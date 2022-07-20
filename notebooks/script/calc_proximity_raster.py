import os
import sys
import rasterio
import subprocess
import argparse

def create_empty_raster(dem_path, proximity_path):
    cmd_create = f'gdal_create -if {dem_path} {proximity_path}'
    subprocess.run(cmd_create, shell=True)

def preprocess_vector_layer(vector_path, dem_path, epsg):
    bounds = rasterio.open(dem_path).bounds   
    extent_dem = f"{bounds[0]}  {bounds[1]} {bounds[2]} {bounds[3]}"
    height, width = rasterio.open(dem_path).shape
    cmd_rasterize = f'gdal_rasterize -burn 255 -ot Byte -ts {width} {height}  -te {extent_dem} {vector_path} rasterized.tif'
    subprocess.run(cmd_rasterize, shell=True)

def calc_proximity_raster(proximity_path, dem_path, vector_path, values=255, maxdist=50000, nodata=-999):
    create_empty_raster(dem_path, proximity_path)
    preprocess_vector_layer(vector_path, dem_path, 32616)
    cmd_proximity = f'gdal_proximity.py -values {values} -distunits GEO -maxdist {maxdist} -nodata {nodata}  rasterized.tif {proximity_path} -co COMPRESS=DEFLATE -co BIGTIFF=YES -co TILED=YES'
    subprocess.run(cmd_proximity, shell=True)
    os.remove('rasterized.tif')
    import glob
    for f in glob.glob("vector_path_proj.*"):
        os.remove(f)

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Download weather data from Modis and CHIRPS",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--dem_path", help="DEM path"
    )
    parser.add_argument(
        "--vector_path", help="path to reference vector layer"
    )
    parser.add_argument(
        "--proximity_path", help="path to raster layer with proximity calculation"
    )
    return parser.parse_args(args), parser

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args, parser = parse_args(args)

    print(f'DEM: {args.dem_path}')
    print(f'VECTOR: {args.vector_path}')
    print(f'PROXIMITY: {args.proximity_path}')
    calc_proximity_raster(args.proximity_path, args.dem_path, args.vector_path)

def run():
    """Entry point for console_scripts"""
    main(sys.argv[1:])

if __name__ == "__main__":
    run()

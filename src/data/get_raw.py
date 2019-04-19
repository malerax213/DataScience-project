# -*- coding: utf-8 -*-
import click
import logging

from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import requests
import shutil


@click.command()
@click.argument('output_filepath', type=click.Path(exists=True))
def main(output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """

    logger = logging.getLogger(__name__)
    logger.info('Getting data from web')

    # We'll get Booking-20181025-1232.csv and Booking-20151012-1322.csv
    urls = ['https://datasource.kapsarc.org/explore/dataset/population-estimates-and-projections-1960-2050/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true','https://datasource.kapsarc.org/explore/dataset/kuwait-population-estimates/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true','https://datasource.kapsarc.org/explore/dataset/population-projections/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true','https://datasource.kapsarc.org/explore/dataset/u-s-regional-annual-population-estimates/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true', 'https://datasource.kapsarc.org/explore/dataset/world-urbanization-prospects-the-2018-revision-population/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true']
    filenames = ['population-estimates-and-projections-1960-2050.csv','kuwait-population-estimates.csv','population-projections.csv','u-s-regional-annual-population-estimates.csv','world-urbanization-prospects-the-2018-revision-population.csv']
    i = 0
    for url in urls:
        r1 = requests.get(url, stream=True)
        if r1.status_code == 200:
            with open(output_filepath+"/"+filenames[i], "wb") as f:
                r1.raw.decode_content = True
                shutil.copyfileobj(r1.raw, f)
                i = i + 1


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

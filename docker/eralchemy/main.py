# -*- coding: utf-8 -*-

import sys
import os
import argparse
import traceback
import logging
import shutil
from cStringIO import StringIO
from datetime import datetime
from datetime import timedelta, tzinfo
from eralchemy import render_er
import psycopg2
import yaml

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)
logger.addHandler(ch)


db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

class JST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=9)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'JST'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", help="output pdf file.")
    args = parser.parse_args()

    os.getcwd()
    current = datetime.now(tz=JST())
    if args.out is None:
        out_target = "%s/eralchemy/%s-%s.pdf" % (os.getcwd(), db_name, current.strftime("%Y-%m-%d_%H%M%S"))
    else:
        out_target = args.out


    df = open("exclude.yml", "r+")
    excludes = " ".join(yaml.load(df)['exclude_tables'])
    connect_url = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (db_user,
                                                            db_password,
                                                            db_host,
                                                            db_port,
                                                            db_name
                                                            )

    logger.info("start : %s ---> %s" % (connect_url, out_target))

    render_er(connect_url, out_target, exclude=excludes)

if __name__ == '__main__':
    main()

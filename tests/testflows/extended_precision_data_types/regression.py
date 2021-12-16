#!/usr/bin/env python3
import os
import sys

from testflows.core import *

append_path(sys.path, "..")

from extended_precision_data_types.requirements import *
from helpers.argparser import argparser
from helpers.cluster import Cluster

xfails = {
}

xflags = {
}

@TestModule
@ArgumentParser(argparser)
@XFails(xfails)
@XFlags(xflags)
@Name("extended precision data types")
@Specifications(
    SRS020_ClickHouse_Extended_Precision_Data_Types
)
@Requirements(
    RQ_SRS_020_ClickHouse_Extended_Precision("1.0"),
)
def regression(self, local, clickhouse_binary_path, stress=None):
    """Extended precision data type regression.
    """
    nodes = {
        "clickhouse":
            ("clickhouse1",)
    }

    with Cluster(local, clickhouse_binary_path, nodes=nodes,
            docker_compose_project_dir=os.path.join(current_dir(), "extended-precision-data-type_env")) as cluster:

        self.context.cluster = cluster
        self.context.stress = stress

        Feature(run=load("extended_precision_data_types.tests.feature", "feature"))

if main():
    regression()

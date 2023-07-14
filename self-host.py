# diagram.py
from diagrams import Diagram, Cluster

from diagrams.generic.storage import Storage
from diagrams.programming.language import PHP
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.compute import GCF
from diagrams.onprem.container import Docker
from diagrams.custom import Custom
from diagrams.gcp.analytics import BigQuery

from diagrams.onprem.inmemory import Redis

from diagrams.onprem.network import Nginx
from diagrams.onprem.database import Mysql



with Diagram("Personal", show=True, direction="LR"):

    

    with Cluster("On Premise" , direction="RL"):
        with Cluster("Rp4"):
            pihole = Custom("PiHole", "./extras/pihole.png")
            passbolt = Custom("passbolt", "./extras/passbolt.png")
            redis = Redis("Redis")

    with Cluster("Oracle Cloud", direction="RL"):
        with Cluster("VM1"):
            hosting = Nginx("Hosting")
            db = Mysql("DB")



#    [ga,fb,hub]>>airbyte >> db >> dashbaord
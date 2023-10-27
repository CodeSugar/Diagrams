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



with Diagram("Personal", show=False, direction="LR"):

    with Cluster("On Premise" ):
        with Cluster("Rp4"):
            caddy = Custom("caddy", "./extras/caddy.png")
            dashboard = Custom("dashboard", "./extras/dashboard.png")
            passbolt = Custom("passbolt", "./extras/passbolt.png")
            redis = Redis("Redis")
        with Cluster("Graveyard"):
            pihole = Custom("PiHole", "./extras/pihole.png")
            penpot = Custom("Penpot", "./extras/penpot.png")
        caddy >> [dashboard,passbolt] 


    with Cluster("Oracle Cloud", direction="RL"):
        with Cluster("VM1"):
            hosting = Nginx("Hosting")
            db = Mysql("DB")



#    [ga,fb,hub]>>airbyte >> db >> dashbaor
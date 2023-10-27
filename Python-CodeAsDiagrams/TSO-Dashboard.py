# diagram.py
from diagrams import Diagram, Cluster

from diagrams.generic.storage import Storage
from diagrams.programming.language import PHP
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.compute import GCF
from diagrams.onprem.container import Docker
from diagrams.custom import Custom
from diagrams.gcp.analytics import BigQuery




with Diagram("TSO - Dashboard", show=True, direction="LR"):

    

    with Cluster("On Premise"):
        airbyte = Custom("Airbyte", "./extras/airbyte.png")

    with Cluster("Google Cloud"):
        db = BigQuery("Database\nAutomated SQL")
        dashbaord = Custom("Dashboard", "./extras/googledatastudio.png")


    with Cluster("Sources",direction="RL"):
        ga = Custom("Gooogle", "./extras/google-analytics.png") 
        fb = Custom("Facebook", "./extras/facebook.png") 
        hub = Custom("Hubspot", "./extras/hubspot.png") 

    [ga,fb,hub]>>airbyte >> db >> dashbaord
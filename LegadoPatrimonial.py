# diagram.py
from diagrams import Diagram, Cluster

from diagrams.generic.storage import Storage
from diagrams.programming.language import PHP
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.compute import GCF
from diagrams.onprem.container import Docker

with Diagram("PDF's Generator", show=True, direction="LR"):

    with Cluster("Webflow"):
        web = Storage("WebSite")

    with Cluster("Hosting 1"):
        webhook = PHP("Webhook\nUpdates")
        node1 = Storage("Storage\n- PDF's\n- Stateless\nAuxiliary Data")

            
    with Cluster("Google Cloud"):
        pub = PubSub("Queue Actions")
        fun =  GCF("Update PDF's")    
    
    with Cluster("Raspberry Local"):
        WA = Docker("WhatsApp Bot")

    web >> webhook >> pub >> fun >> pub >> WA

    fun >> node1

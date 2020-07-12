import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template


class Declencheur(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print(" behavior commence ... ")
           
        async def run(self):
            msg = Message(to="scrapper@xmpp.jp")     
            msg.set_metadata("performative", "inform") 
            msg.body = "commmence le scrapping"                    

            await self.send(msg)
            print("Message sent!")
            await asyncio.sleep(3600) #attendre une heure

    async def setup(self):
        print("l'agent déclencheur commence . . .")
        b = self.MyBehav()
        self.add_behaviour(b)

  
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
import time

class Scrapper(Agent):
    class RecvBehav(CyclicBehaviour):
        async def run(self):
            print("RecvBehav commence . .. ")

            msg = await self.receive(timeout=20) # attendre le message 20 sec
            if msg:
                print("Message bien recu : {}".format(msg.body))

                response = requests.get('https://www.challenge.ma/lessentiel/')
                soup = BeautifulSoup(response.text, 'html.parser')

                rows = soup.findAll("div", {"class": "vw-block-grid-item"})
                
                posts = []

                for row in rows:
                    moreInfo = row.h3.find('a', href=True)
                    data = {
                        'title': row.h3.a.getText(),
                        'body': row.p.getText(),
                        'time': row.time.getText(),
                        'more': moreInfo['href']
                    }
                    posts.append(data)
                responseData = {'news': posts}
            else:
                print("aucun message recu")

            # stop agent from behaviour
            await asyncio.sleep(80)

    async def setup(self):
        print("Agent scrapper demarre")
        b = self.RecvBehav()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

import json
import time


from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Scope:")
        print(self.scope)
        # self.room_name=self.scope["url_route"]["kwargs"]["room_name"]
        # self.room_group_name="chat_%s" % self.room_name

        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name, self.channel_name
        # )

        self.accept()
        self.send(json.dumps({"message": "Message from the server:  WebSocket Established.  Assuming app connected to LN node."}))
       

    def disconnect(self, close_code):
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name, self.channel_name
        #)
        pass
    
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message = text_data_json["message"]

        #async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type":"chat_message", "message":message}
        self.test_method(message)

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message":message}))


    def test_method(self, message):
        print("In the test")
        time.sleep(7)
        l=[1,2,3]
        for i in l:
            if i==1:
                print("1")
                self.send(text_data=json.dumps({"message": "Message from the Server:  Simulated Open Channel Request Sent to LN Node."}))
            if i==2:
                print("2")
                self.send(text_data=json.dumps({"message": "Message from the Server:  Simulated Received from LN Node: Open Channel Pending..."}))
            if i==3:
                print("3")
                self.send(text_data=json.dumps({"message": "Message from the Server:  Simulated Received from the LN Node: Channel Open!"}))
            time.sleep(7)


# chat/consumers.py  asynchronous 
# import json

# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = "chat_%s" % self.room_name

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     def jls_extract_def(self, scope):
#         return scope

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         print(message)
#         print(self.scope["path"])
#         print(self.scope["headers"])
#         print("*******")
#         print(self.scope)
#         print("%%%%%")
#         print(text_data)

#         r=True
#         if message=="Hi Titan!Hi Titan!Hi Titan!":

#             await self.send(text_data=json.dumps({"message": "Opening"}))
#             print("**")
#             await self.test_method(message)
#         else:
#             await self.send(text_data=json.dumps({"message": "no"}))
#             time.sleep(5)
#             print("@@@")

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat_message", "message": message}
#         )
#     async def respond1(self):
#         await async_to_sync(self.send)(text_data=json.dumps({"message": "Message1"}))
#         print("respond1")

#     async def respond2(self):
#         await async_to_sync(self.send)(text_data=json.dumps({"message": "Message2"}))
#         print("respond2")

#     async def respond3(self):
#         await async_to_sync(self.send)(text_data=json.dumps({"message": "Message3"}))
#         print("respond3")

#     async def test_method(self, message):
#         print("In the test")
#         l=[1,2,3]
#         for i in l:
#             if i==1:
#                 print("1")
#                 await self.send(text_data=json.dumps({"message": "Message1"}))
#             if i==2:
#                 print("2")
#                 await self.send(text_data=json.dumps({"message": "Message2"}))
#             if i==3:
#                 print("3")
#                 await self.send(text_data=json.dumps({"message": "Message3"}))
#             time.sleep(5)



    


#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))
        
    
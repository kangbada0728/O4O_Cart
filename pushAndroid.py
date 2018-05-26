from pyfcm import FCMNotification

#앱이 깔릴때 API_KEY가 할당된다.
API_KEY = "AAAAMPLTW5s:APA91bF-UhyG6r2Y50WX5UE7bNCKKWYTZJFZA8qtKgOVGly_MEhgfnDUI8spG8myIZcwiVCVHOP_EUxHuXTDl1yhwMv8Cr5I6u9ZWF2D0iGOTyDqZhOyOWYvZCMZ-jBRQMs92mE2RkoO"

push_service = FCMNotification(api_key=API_KEY)

'''data = {
        "title":"mytitle",
        "body":"mybody",
        "url":"myurl"
        }
'''
registration_id = "dpLpgO-yYmQ:APA91bGdZALuiVNMLBfVkR7fjQjwQnWQlcU0WQK1b0wR9j5lfJvZ0lwS2MBQq7MXLLiQFjrLFGs-5cT9wnB8W73gz9K3iVW_k24E0_FLn025eBXbutk2nH5meU-cKLB8n0vprHUA4v4g"
message_title = "coupon"
message_body = "pushNotification"

#print(push_service.notify_topic_subscribers(topic_name="notice", data_message=data))
result = push_service.notify_single_device(registration_id=registration_id,message_title=message_title,message_body=message_body)
print(result)
from pyfcm import FCMNotification

API_KEY = "AAAAgOST7Pg:APA91bErWBhskXNrRXZezZ2dO5_KpBrTFbD962vq9yLTNwV-Z-IPGr2e2UMWPTzy2uo7sL0H0aaf8lPTnEPbPf3YZsbT1By1KIIUK94O9qV9Dr2zQuoQ5Ah__ITirE3LItMukwHCE-eS"

push_service = FCMNotification(api_key=API_KEY)

'''data = {
        "title":"mytitle",
        "body":"mybody",
        "url":"myurl"
        }
'''
registration_id = "dIxEhXavQSg:APA91bHQHgLRsUnrkswmWS051h_ggpvHTbQAYVshtlWvOiozn2WZZCynqHvNlc5877thiO-Oc8VHqW1uIUmMMJaV0mzaeTRL2UNRxNoP9EtnZxIV2EWtKMdH_Wc3ZKMMsbRW50zCRRoU"
message_title = "coupon"
message_body = "pushNotification"

#print(push_service.notify_topic_subscribers(topic_name="notice", data_message=data))
result = push_service.notify_single_device(registration_id=registration_id,message_title=message_title,message_body=message_body)
print(result)

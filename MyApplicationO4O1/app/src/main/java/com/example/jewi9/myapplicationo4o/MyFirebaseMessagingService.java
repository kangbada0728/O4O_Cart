package com.example.jewi9.myapplicationo4o;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.media.RingtoneManager;
import android.net.Uri;

import android.support.v4.app.NotificationCompat;
import android.util.Log;

import com.google.firebase.messaging.RemoteMessage;

import org.json.JSONObject;


public class MyFirebaseMessagingService extends com.google.firebase.messaging.FirebaseMessagingService {
    private static final String TAG = "FirebaseMsgService";
    public static JSONObject pushData=null;
    // [START receive_message]
    @Override
    public void onMessageReceived(RemoteMessage remoteMessage)   {
        //Intent intent = new Intent(MyFirebaseMessagingService.this,Push.class);
        //startActivity(intent);
        if (remoteMessage.getData().size() > 0) {
            sendNotification(remoteMessage.getData().get("message"));
        }

        if (remoteMessage.getNotification() != null) {
            sendNotification(remoteMessage.getNotification().getBody());

            Log.d("Link@@@@@@","Link@@@@@@"+remoteMessage.getData());
        }
        pushData = new JSONObject(remoteMessage.getData());
        Log.d("Link@@@@@@","Link@@@@@@"+pushData);

        //sendNotification(remoteMessage.getData().get("message"));
    }

    private void sendNotification(String message) {
        System.out.println("@@@@@@received message in sendNotification : " + message);

        Intent intent = new Intent(this, CheckWatchAd.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0 /* Request code */, intent,
                PendingIntent.FLAG_ONE_SHOT);


        String channelId = "channel Id";
        Uri defaultSoundUri= RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
        NotificationCompat.Builder notificationBuilder = new NotificationCompat.Builder(this,channelId)
                .setSmallIcon(R.drawable.o4o)
                .setContentTitle("O4O CART 광고가 도착했습니다.")
                .setContentText(message)
                .setAutoCancel(true)
                .setSound(defaultSoundUri)
                .setContentIntent(pendingIntent);

        NotificationManager notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);

        //owerManager pm = (PowerManager) this.getSystemService(Context.POWER_SERVICE);
        //PowerManager.WakeLock wakelock = pm.newWakeLock(PowerManager.FULL_WAKE_LOCK | PowerManager.ACQUIRE_CAUSES_WAKEUP, "TAG");
        //wakelock.acquire(5000);

        notificationManager.notify(0 /* ID of notification */, notificationBuilder.build());
    }
}
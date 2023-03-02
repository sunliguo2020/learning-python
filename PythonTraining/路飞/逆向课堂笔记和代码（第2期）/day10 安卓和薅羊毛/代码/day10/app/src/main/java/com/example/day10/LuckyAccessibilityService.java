package com.example.day10;

import android.accessibilityservice.AccessibilityService;
import android.accessibilityservice.GestureDescription;
import android.graphics.Path;
import android.os.Bundle;
import android.util.Log;
import android.view.accessibility.AccessibilityEvent;
import android.view.accessibility.AccessibilityNodeInfo;

import androidx.core.view.accessibility.AccessibilityNodeInfoCompat;

import java.util.List;

public class LuckyAccessibilityService extends AccessibilityService {

    public static boolean allowStart = false;
    public static boolean running = false;

    public static boolean isOpenDouYin = false;

    @Override
    public void onInterrupt() {

    }


    @Override
    public void onAccessibilityEvent(AccessibilityEvent event) {
        // 手机内部自动触发调用，手机有一些变动，自动执行（系统）
        Log.e("无障碍", "来了");
        // 开启无障碍模式后，方法会自动调用（寻找相关标签、点击、欢动）
        if (!allowStart) {
            return;
        }

        if (!running) {
            running = true;
            // 创建线程去执行抖音薅羊毛任务（只有一个线程）
            new Thread(new Runnable() {
                @Override
                public void run() {
                    // 后续代码（新创建一个线程 + 防止创建很多线程）
                    Log.e("无障碍", "开始运行");

                    douYinTask();
                }
            }).start();
        }

    }

    /**
     * 抖音的操作
     */
    public void douYinTask() {
        try {
            while (true) {

                trainTask();

                // 红包、福袋

            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    /**
     * 养好
     */
    public void trainTask() throws InterruptedException {
        if (!isOpenDouYin) {
            // 回到首页 & 杀死其他进程
            killAll();
            // 滑动屏幕，寻找抖音app，打开app
            if (findApplicationByName("抖音")) {
                isOpenDouYin = true;
            }
        }
        // 4.滑动屏幕
        Thread.sleep(5000);
        slideScreen(540, 1500, 540, 200, 200L, 100L);
        Thread.sleep(2*1000);
        // 5.点赞
        // 理论：找到点赞标签
        // 抖音：点击（3个）
        doClickFavor();
        Thread.sleep(3*1000);

        // 6.评论
        comment();

        Thread.sleep(2*1000);

        // 7.返回上一步
        performGlobalAction(AccessibilityService.GLOBAL_ACTION_BACK);
        Thread.sleep(2*1000);
    }
    private void comment(){
        try{
            // 评论按钮 & 点击
            AccessibilityNodeInfo node = findNodeByIdAndIndex("com.ss.android.ugc.aweme:id/b9k", 1);
            clickByNodeClickable(node);

            Thread.sleep(2*1000);

            AccessibilityNodeInfo nodeButton = findNodeById("com.ss.android.ugc.aweme:id/b9r");
            clickByNodeClickable(nodeButton);

            Thread.sleep(2*1000);

            inputLuckyCommentText("666");

            Thread.sleep(2*1000);

            submitLuckyCommentText();

            Thread.sleep(2*1000);

        }catch (Exception e){

        }
    }

    private boolean submitLuckyCommentText() {
        try {
            AccessibilityNodeInfo node = findNodeById("com.ss.android.ugc.aweme:id/b_j");
            clickByNodeClickable(node);
            return true;
        } catch (Exception e) {
            Log.e("无障碍", "【异常】提交评论");
        }
        return false;
    }


    private boolean inputLuckyCommentText(String text) {
        try {
            AccessibilityNodeInfo editNode = findNodeById("com.ss.android.ugc.aweme:id/b9r");

            Bundle arguments = new Bundle();
            arguments.putString(AccessibilityNodeInfoCompat.ACTION_ARGUMENT_SET_TEXT_CHARSEQUENCE, text);
            editNode.performAction(AccessibilityNodeInfoCompat.ACTION_SET_TEXT, arguments);
            return true;
        } catch (Exception e) {
            Log.e("无障碍", "【异常】输入评论内容");
        }
        return false;
    }

    private boolean doClickFavor() {
        try {
            AccessibilityNodeInfo node = findNodeByIdAndIndex("com.ss.android.ugc.aweme:id/bwc", 1);
            if (node != null) {
                // 点击
                clickByNodeClickable(node);
                return true;
            } else {
                Log.e("无障碍", "【失败】点赞，未找到点赞按钮。");
            }
        } catch (Exception e) {
            Log.e("无障碍", "【异常】点赞，详细原因：" + e.toString());
        }
        return false;
    }


    public void killAll() throws InterruptedException {
        // 1.回到首页 Home
        performGlobalAction(GLOBAL_ACTION_HOME);
        Thread.sleep(2000);
        performGlobalAction(GLOBAL_ACTION_HOME);
        Thread.sleep(2000);

        // 杀死其他应用
        performGlobalAction(GLOBAL_ACTION_RECENTS);
        Thread.sleep(2000);

        String[] clearAppIdArray = new String[]{
                "com.huawei.android.launcher:id/clear_all_recents_image_button", // 华为v30 pro
                "com.android.systemui:id/clearAnimView" // 小米8A
        };
        for (String id : clearAppIdArray) {
            // 根据ID找到节点
            AccessibilityNodeInfo clearIdNode = findNodeById(id);
            if (clearIdNode != null) {
                // 点击标签
                clickByNodeClickable(clearIdNode);
                break;
            }
        }
    }

    public static void startTask() {
        allowStart = true;
    }

    /**
     * 根据ID找元素
     */
    private AccessibilityNodeInfo findNodeById(String id) {
        AccessibilityNodeInfo root = getRootInActiveWindow();
        if (root == null) {
            return null;
        }
        List<AccessibilityNodeInfo> nodeList = root.findAccessibilityNodeInfosByViewId(id);
        if (nodeList != null) {
            for (int i = 0; i < nodeList.size(); i++) {
                AccessibilityNodeInfo node = nodeList.get(i);
                if (node != null) {
                    return node;
                }
            }
        }
        return null;
    }

    /**
     * 根据文本找元素
     */
    private AccessibilityNodeInfo findNodeByText(String text) {
        AccessibilityNodeInfo root = getRootInActiveWindow();
        if (root == null) {
            return null;
        }
        List<AccessibilityNodeInfo> nodeList = root.findAccessibilityNodeInfosByText(text);
        if (nodeList != null) {
            for (int i = 0; i < nodeList.size(); i++) {
                AccessibilityNodeInfo node = nodeList.get(i);
                if (node != null) {
                    return node;
                }
            }
        }
        return null;
    }

    /**
     * 根据ID找元素 + 索引获取执行元素
     */
    private AccessibilityNodeInfo findNodeByIdAndIndex(String id, int index) {
        AccessibilityNodeInfo root = getRootInActiveWindow();
        List<AccessibilityNodeInfo> nodeList = root.findAccessibilityNodeInfosByViewId(id);
        if (nodeList != null) {
            AccessibilityNodeInfo node = nodeList.get(index);
            return node;
        }
        return null;
    }

    /**
     * 点击节点 点击
     */
    private void clickByNodeClickable(AccessibilityNodeInfo node) {
        if (node.isClickable()) {
            node.performAction(AccessibilityNodeInfo.ACTION_CLICK);
            node.recycle();
        } else {
            AccessibilityNodeInfo parent = node.getParent();
            node.recycle();
            clickByNodeClickable(parent);
        }
    }


    /**
     * 在页面上寻找名字叫啥的app
     *
     * @param name
     * @return
     * @throws InterruptedException
     */
    public boolean findApplicationByName(String name) throws InterruptedException {
        while (true) {
            // 翻看右边的页面
            slideScreen(540, 800, 100, 800, 500L, 200L);
            Thread.sleep(3000);

            // 找抖音APP
            AccessibilityNodeInfo app = findNodeByText(name);
            if (app != null) {
                Thread.sleep(500);
                clickByNodeClickable(app);
                Thread.sleep(5000);
                return true;
            }
        }
    }

    /**
     * 滑动屏幕
     */
    private boolean slideScreen(int startX, int startY, int endX, int endY, Long startTime, Long duration) {
        try {
            Path path = new Path();
            path.moveTo(startX, startY);
            path.lineTo(endX, endY);
            GestureDescription.Builder builder = new GestureDescription.Builder();
            // GestureDescription description = builder.addStroke(new GestureDescription.StrokeDescription(path, 500L, 37L)).build();
            // GestureDescription description = builder.addStroke(new GestureDescription.StrokeDescription(path, 1000L, 500L)).build();
            GestureDescription description = builder.addStroke(new GestureDescription.StrokeDescription(path, startTime, duration)).build();
            dispatchGesture(description, null, null);
            return true;
        } catch (Exception e) {
            // Log.e(TAG, "滑动屏幕失败，详细：" + e.toString());
            Log.e("无障碍", "滑动屏幕失败");
        }
        return false;
    }

}

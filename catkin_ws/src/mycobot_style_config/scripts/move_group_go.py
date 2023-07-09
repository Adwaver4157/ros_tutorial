#!/usr/bin/env python3
# coding: UTF-8
import moveit_commander
import rospy
import sys
import numpy as np
from math import pi


def main():
    # moveit_commanderの初期化
    moveit_commander.roscpp_initialize(sys.argv)

    # ノードの初期化
    rospy.init_node('move_group_go')

    # MoveGroupCommanderのインスタンス化
    move_group = moveit_commander.MoveGroupCommander("mycobot_style_arm")

    # 現在の関節角度を取得
    joint_goal = move_group.get_current_joint_values()
    print("from:", np.rad2deg(joint_goal))

    # 関節角度の指定
    joint_goal[0] = 0
    joint_goal[1] = 80 * pi / 180
    joint_goal[2] = 80 * pi / 180
    joint_goal[3] = 0
    print("to:", np.rad2deg(joint_goal))

    # 関節角度によるモーションプランニングと動作の実行
    move_group.go(joint_goal, wait=True)

    # 停止 (動きが残っていないことを保証)
    move_group.stop()


if __name__ == "__main__":
    main()

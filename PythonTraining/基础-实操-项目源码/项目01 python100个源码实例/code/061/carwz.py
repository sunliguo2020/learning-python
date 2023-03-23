import requests

def main():
    """
    主函数
    :return: None
    """
    # 请求网址
    url = "http://carwz.shumaidata.com/post/carwz"
    # 接口appcode
    appcode = 'fd1dfdc3c97447f6b5259ebaf51808f7'
    # headers信息
    headers = {'Authorization': f'APPCODE {appcode}'}
    # 请求数据
    data = {
        'car_no': car_no,
        'car_type': car_type,
        'engine_number': engine_number,
        'frame_number': frame_number
    }

    try:
        # 发送post请求
        response = requests.post(url, params=data, headers=headers)
        content = response.json() # 获取json数据
        if content["code"] != '0':
            print("请求失败,请检查您的输入信息")
            return
        carNo = content["result"]["carNo"] # 获取车牌号
        if content["result"]["vioNum"] == "0":
            print(f"您的车牌号{carNo}没有违章记录")
        else:
            print(f"您的车牌号{carNo}有如下违章记录")
            # 遍历违章记录
            for item in content["result"]["data"]:
                print("*" * 20)
                print(f"""
违章时间: {item["vioTime"]}
违章地点: {item["vioAddress"]}
违章原因: {item["vioAction"]}
罚款金额: {item["vioFine"]}
罚款扣分: {item["vioScore"]}
                """)
    except:
        print("请求异常")

if __name__  == "__main__":
    # 用户输入车辆查询相关数据
    car_no = input("请输入如车牌号：")
    car_type = input("请输入如车辆类型，大车输入01，小车输入02：")
    engine_number = input("请输入如车辆引擎号：")
    frame_number = input("请输入如车架号：")
    # 调用主函数
    main()
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2026/1/26 13:03
"""
import os
import pandas as pd

# ==================== 自定义部分 ====================
original_file_path = r"D:\桌面\现代中学监控IP表新编IP-20260126.xlsx"  # 原文件（只读）
result_file_path = r"D:\桌面\IP-录像机匹配结果.xlsx"  # 最终结果文件（仅两列）
summary_sheet = "汇总"  # 汇总表名称
summary_ip_colname = "IP地址"  # 汇总表IP列的列名
dvr_ip_colname = "IP地址"  # 录像机表IP列的列名
exclude_sheets = [summary_sheet, "arp", "搜索", "海康", "密码", "录像机IP"]
# ====================================================

try:
    # 第一步：读取汇总表的所有IP地址（仅提取IP列）
    df_summary = pd.read_excel(original_file_path, sheet_name=summary_sheet, header=0)
    print(f"📌 汇总表实际列名：{list(df_summary.columns)}")

    # 检查汇总表IP列是否存在
    if summary_ip_colname not in df_summary.columns:
        raise ValueError(f"汇总表中未找到列名：{summary_ip_colname}，请核对表头！")

    # 提取IP列并去重、过滤空值，生成基础结果表
    ip_series = df_summary[summary_ip_colname].dropna().astype(str)  # 转字符串
    ip_series = ip_series[ip_series.str.strip() != ""]  # 过滤空字符串
    df_result = pd.DataFrame({
        "IP地址": ip_series.unique(),  # 去重，仅保留唯一IP
        "所属录像机": "未找到"  # 初始化结果列
    })
    print(f"\n📌 从汇总表提取到 {len(df_result)} 个有效IP地址")

    # 第二步：读取原文件的所有录像机工作表名称
    excel_file = pd.ExcelFile(original_file_path)
    dvr_sheets = [sheet for sheet in excel_file.sheet_names if sheet not in exclude_sheets]
    processed_sheets = 0

    print(f"\n📌 待处理的录像机工作表：{dvr_sheets}")

    # 第三步：遍历每个录像机工作表，匹配IP并填充所属录像机
    for dvr_sheet in dvr_sheets:
        try:
            # 读取录像机表的IP列
            df_dvr = pd.read_excel(original_file_path, sheet_name=dvr_sheet, header=0)
            print(f"\n🔍 工作表 {dvr_sheet} 列名：{list(df_dvr.columns)}")

            # 检查录像机表IP列是否存在
            if dvr_ip_colname not in df_dvr.columns:
                print(f"⚠️  工作表 {dvr_sheet} 中未找到{dvr_ip_colname}列，跳过该表")
                continue

            # 提取有效IP（去重、过滤空值、转字符串）
            dvr_ips = df_dvr[dvr_ip_colname].dropna().astype(str).unique()
            dvr_ips = [ip.strip() for ip in dvr_ips if ip.strip() != ""]
            if len(dvr_ips) == 0:
                print(f"⚠️  工作表 {dvr_sheet} 无有效IP，跳过")
                continue

            # 匹配IP并填充录像机名称
            mask = df_result["IP地址"].isin(dvr_ips)
            match_count = mask.sum()
            df_result.loc[mask & (df_result["所属录像机"] == "未找到"), "所属录像机"] = dvr_sheet

            processed_sheets += 1
            print(f"✅ 成功处理 {dvr_sheet}：匹配到 {match_count} 个IP")

        except Exception as e:
            print(f"❌ 处理 {dvr_sheet} 出错：{str(e)[:80]}")
            continue

    # 第四步：保存极简结果文件（仅两列）
    # 删除旧的结果文件（避免残留）
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
    # 保存新文件，不保留索引
    df_result.to_excel(result_file_path, index=False)

    # 统计匹配结果
    matched_count = len(df_result[df_result["所属录像机"] != "未找到"])
    unmatched_count = len(df_result) - matched_count

    # 输出最终统计信息
    print("\n" + "=" * 60)
    print(f"📌 IP-录像机匹配完成！")
    print(f"📁 结果文件：{result_file_path}（仅包含IP地址、所属录像机两列）")
    print(f"📊 总计扫描 {len(dvr_sheets)} 个录像机工作表")
    print(f"✅ 成功处理 {processed_sheets} 个工作表")
    print(f"📈 匹配结果：")
    print(f"   - 总有效IP数：{len(df_result)}")
    print(f"   - 匹配成功：{matched_count} 个IP")
    print(f"   - 未匹配到：{unmatched_count} 个IP（标注为“未找到”）")

except FileNotFoundError:
    print(f"❌ 错误：未找到原文件 → {original_file_path}")
    print("请检查文件路径是否正确，文件名是否有拼写错误")
except PermissionError:
    print(f"❌ 错误：无权限操作文件！")
    print("解决方法：1. 关闭WPS/Excel中打开的结果文件  2. 以管理员身份运行脚本")
except ValueError as e:
    print(f"❌ 配置错误：{e}")
except Exception as e:
    print(f"❌ 程序运行出错：{str(e)[:100]}")
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import ttk
import random

questions_db = {
    "第一单元": [
        {"question": "住房的基本结构包括______、______、______、______。", "answer": "框架、承重、户型、采光"},
        {"question": "住房系统中负责废水排放的是______系统。", "answer": "排水"},
        {"question": "港珠澳大桥总长度是______千米，包含______、______、______三种结构。", "answer": "55、桥、岛、隧"},
        {"question": "工程设计的核心环节是______。", "answer": "设计"},
        {"question": "塔台标书必须包含______、______、______三个核心要素。", "answer": "成本预算、安全性、设计图"},
        {"question": "三角形结构比四边形更______。", "answer": "稳定"},
        {"question": "测试塔台模型时需要统一______、______、______。", "answer": "方法、标准、工具"},
        {"question": "抗震设计的三种方法：______、______、______。", "answer": "耐震、制震、免震"},
        {"question": "塔台模型制作流程：设计→______→______→评估→改进。", "answer": "制作、测试"},
        {"question": "埃菲尔铁塔采用大量______结构增强稳定性。", "answer": "三角形"},
        {"question": "工程竞标通过______方式选择方案。", "answer": "竞标"},
        {"question": "塔台选址要求：______和______。", "answer": "无视野遮挡、地面高地"},
        {"question": "四边形加固需要增加______结构。", "answer": "斜杆"},
        {"question": "工程实施推动______发展。", "answer": "技术"},
        {"question": "塔台成本控制需要减少______和______的使用。", "answer": "吸管、胶带"},
        {"question": "模型测试中发现塔台倾斜，可能因为立柱______不等高。", "answer": "高度"},
        {"question": "抗风设计应采用______结构。", "answer": "框架"},
        {"question": "评估模型时需要开展______评估和______评估。", "answer": "自我、组间"},
        {"question": "塔台底座应遵循______原则。", "answer": "上小下大、上轻下重"},
        {"question": "工程验收属于建造流程的______阶段。", "answer": "最后"}
    ],
    "第二单元": [
        {"question": "调查地下生物需要携带______和______。", "answer": "小铲、放大镜"},
        {"question": "通过动物______可以推测其存在。", "answer": "粪便/毛发/脚印"},
        {"question": "二歧分类法的分类依据是______特征。", "answer": "不同"},
        {"question": "杂交水稻利用了生物的______特性。", "answer": "遗传变异"},
        {"question": "哺乳动物的特征是______和______。", "answer": "胎生、哺乳"},
        {"question": "化石能反映古生物的______环境。", "answer": "生活"},
        {"question": "人的性状包括______、______等。", "answer": "耳垂、单双眼皮"},
        {"question": "红绿色盲属于______疾病。", "answer": "可遗传"},
        {"question": "制作校园生物分布图需要记录生物的______和______。", "answer": "种类、数量"},
        {"question": "昆虫的身体有______对足。", "answer": "3"},
        {"question": "鸟类具有______和______特征。", "answer": "羽毛、卵生"},
        {"question": "生物多样性包含______价值和______价值。", "answer": "直接、间接"},
        {"question": "保护生物多样性的措施包括建立______。", "answer": "自然保护区"},
        {"question": "比较亲代与后代可观察______的异同。", "answer": "叶形/花色"},
        {"question": "恐龙化石表明其与______有亲缘关系。", "answer": "鸟类"},
        {"question": "植物光合作用产生______。", "answer": "氧气"},
        {"question": "遗传物质通过______传递给后代。", "answer": "种子/器官"},
        {"question": "鱼类用______呼吸。", "answer": "鳃"},
        {"question": "生物调查的三个步骤：______、______、______。", "answer": "明确任务、制定方案、实地调查"},
        {"question": "无籽西瓜是______的结果。", "answer": "人工选育"}
    ],
    "第三单元": [
        {"question": "太阳质量占比达______%。", "answer": "99.86"},
        {"question": "日食发生时三者的位置顺序：______→______→______。", "answer": "日、月、地"},
        {"question": "北极星位于______星座。", "answer": "小熊"},
        {"question": "夏季大三角包含______、______、______三颗星。", "answer": "天津四、织女星、牛郎星"},
        {"question": "太阳系最外侧的行星是______。", "answer": "海王星"},
        {"question": "星座是恒星的______图像。", "answer": "视觉"},
        {"question": "木星的特征是______大、______周期短。", "answer": "体积、自转"},
...         {"question": "人类登月探测器叫______号。", "answer": "嫦娥"},
...         {"question": "银河系包含______颗恒星。", "answer": "2000-4000亿"},
...         {"question": "观星盘需对准______星座。", "answer": "大熊"},
...         {"question": "全天划分为______个星座。", "answer": "88"},
...         {"question": "金星的自转周期比公转周期______。", "answer": "长"},
...         {"question": "人类第一个空间望远镜是______望远镜。", "answer": "伽利略"},
...         {"question": "我国火星车叫______号。", "answer": "祝融"},
...         {"question": "彗星公转周期最长达______年。", "answer": "数百万"},
...         {"question": "航天时代开始于______世纪。", "answer": "20"},
...         {"question": "北斗七星属于______星座。", "answer": "大熊"},
...         {"question": "月球是地球的______星。", "answer": "卫星"},
...         {"question": "太阳属于______星。", "answer": "恒"},
...         {"question": "银河系直径约______光年。", "answer": "10万"}
...     ],
...     "第四单元": [
...         {"question": "淀粉遇碘变______色，属于______变化。", "answer": "蓝、化学"},
...         {"question": "蜡烛燃烧产生______和______两种变化。", "answer": "物理、化学"},
...         {"question": "煤的形成需要______和______条件。", "answer": "高温、高压"},
...         {"question": "光合作用将______转化为氧气。", "answer": "二氧化碳"},
...         {"question": "小苏打+白醋产生______气体。", "answer": "二氧化碳"},
...         {"question": "物质变化的根本区别是是否产生______。", "answer": "新物质"},
...         {"question": "咀嚼馒头变甜是因为______酶的作用。", "answer": "唾液淀粉"},
...         {"question": "紫甘蓝遇白醋发生______变化。", "answer": "化学"},
...         {"question": "食物消化属于______变化。", "answer": "化学"},
...         {"question": "岩石形成属于______变化。", "answer": "化学"},
...         {"question": "铁生锈是______变化。", "answer": "化学"},
...         {"question": "水的三态变化是______变化。", "answer": "物理"},
...         {"question": "石油是______长期变化的产物。", "answer": "古代生物"},
...         {"question": "制作柠檬汽水会产生______气体。", "answer": "二氧化碳"},
...         {"question": "判断化学变化的标志：______、______、______、______。", "answer": "发光、发热、变色、产生气体"},
...         {"question": "烟花燃放包含______变化。", "answer": "化学"},
...         {"question": "面包发霉是______变化。", "answer": "化学"},
        {"question": "食盐溶解属于______变化。", "answer": "物理"},
        {"question": "光合作用的能量来源是______。", "answer": "太阳能"},
        {"question": "化学变化对人类既有______也有危害。", "answer": "益处"}
    ]
}

class ScienceQuizApp:
    def __init__(self, root):
        # ...（界面代码与之前相同）...

if __name__ == "__main__":
    root = tk.Tk()
    app = ScienceQuizApp(root)
    root.geometry("500x300")  # 扩大窗口尺寸

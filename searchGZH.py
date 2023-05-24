# import CORS as CORS
import time
import datetime
import requests
import json




# 印象笔记重磅发布了2020年度最具收藏价值公众号Top 50的榜单:
# 时政要闻榜】: 「人民日报」「政事堂2019」「观察者网」「九边」和「远方青木」；「南方周末」「澎湃新闻」「中国新闻周刊」「兔主席」
# 职场学习榜】: 「秋叶PPT」「warfalcon」「罗辑思维」「L先生说」「曹将」「粥左罗」「高杉legal」「孤独大脑」「APPSO」「量子学派」
# 科技财经榜】: 「笔记侠」、「虎嗅」「刘润」「泽平宏观」「36氪」、「雪球」、「机器之心」「第一财经YiMagazine」「招财大牛猫」、「格隆」
# 生活人文榜】: 「三联生活周刊」「丁香医生」「果壳」「KnowYourself」 「地球知识局」 「人物」「半佛仙人」「女神进化论」「兽楼处」「看理想」
# 大象推荐榜】:  「在人间living」「回形针papercilp」「远川研究所」「Philosophia 哲学社」「哲学」「晚点LatePost」「深响」「卢克文工作室」「腿姐考研政治课堂」「RUC新闻坊」「CambCC」


# 1. 新鲜事早知道： 每日推送前天发布的新鲜公众号文章
# 2. 知名公众号内容精选： 每日对单个知名公众号进行独家专栏

# 分不分文章类型 ？
# 评选标准： 看阅读量 ？


def getGzhJson(url, myCookie):
	# cookie need change!
	# myCookie = ''''''
	headers = {
	'cookie': myCookie,
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	}
	try:
		r=requests.get(url, headers = headers)
		r.raise_for_status()
		r.encoding='utf-8'
		return json.loads(r.text)
	except Exception as e:
		print(e)
		return []


def bizList():
	gzhList = [
		# 印象笔记2022最具收藏价值十大公众号
		{"title": "笔记侠",},
		{"title": "刘润", },
		# {"title": "政事堂2021", },
		# {"title": "丁香医生", },
		# {"title": "36氪", },
		# {"title": "秋叶PPT", },
		# {"title": "罗辑思维", },
		# {"title": "卢克文工作室", },
		# {"title": "粥左罗", },
		# {"title": "九边", },

		# 印象笔记评出2021年度最具收藏价值公众号TOP50
		# {"title": "正和岛", },
		# {"title": "观察者网", },
		# {"title": "政事堂2019", },
		# {"title": "泽平宏观", },
		# {"title": "华尔街见闻", },
		# {"title": "大树乡长", },
		# {"title": "灼识新维度", },
		# {"title": "远川研究所", },
		# {"title": "澎湃思想市场", },
		# {"title": "雪球", },
		#
		# {"title": "智谷趋势", },
		# {"title": "研讯社", },
		# {"title": "金融监管研究院", },
		# {"title": "银行螺丝钉", },
		# {"title": "力哥", },
		# {"title": "机器之心", },
		# {"title": "L先生说", },
		# {"title": "KnowYourself", },
		# {"title": "孤独大脑", },
		# {"title": "壹心理", },
		#
		# {"title": "果壳", },
		# {"title": "人物", },
		# {"title": "星球研究所", },
		# {"title": "新潮沉思录", },
		# {"title": "warfalcon", },
		# {"title": "曹将", },
		# {"title": "管理的常识", },
		# {"title": "辉哥奇谭", },
		# {"title": "混沌学园", },
		# {"title": "InfoQ", },
		#
		# {"title": "Excel精英培训", },
		# {"title": "老笔头", },
		# {"title": "半佛仙人", },
		# {"title": "三联生活周刊", },
		# {"title": "地球知识局", },
		# {"title": "原理", },
		# {"title": "连岳", },
		# {"title": "记忆承载", },
		# {"title": "文小叔说", },
		# {"title": "先知书店店长荐书", },
		#
		# {"title": "历史研习社", },
		# {"title": "故事FM", },
		# {"title": "看理想", },
		# {"title": "正面连接", },
		# {"title": "腿姐考研政治课堂", },
		# {"title": "正面连接", },
		# {"title": "地道风物", },
		# {"title": "环行星球", },
		# {"title": "晚点LatePost", },
		# {"title": "徐慢慢心理话", },
		#
		# {"title": "海边的西塞罗", },
		# {"title": "人神共奋", },
	]
	cookie = "appmsglist_action_3089078790=card; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; pgv_info=ssid=s3079674102; pgv_pvid=4885597462; pac_uid=0_c2d564fe23d91; ua_id=ckCXkB8COINwzdn5AAAAAC5s4SIh_xA-ryGJ8I5kaNU=; wxuin=77588568689922; mm_lang=zh_CN; cert=YXgIG3csf2E53xNCTX2MfYL0HlYNHHS0; sig=h01d205d569c9d44197249458020a30ce2fd6129d99e66584d4fda264710280566b994ac6966cebec29; uuid=56ed26ad99950c97f2a4e4717b85b9ab; rand_info=CAESIH0q+ytK7lPSTtylyJ8qpNs7tt1VquWga86CJPKt2Vu2; slave_bizuin=3089078790; data_bizuin=3089078790; bizuin=3089078790; data_ticket=esK8JlgsXIqLA3liSjn+gDAewJ6p6wNoH6++B76ioz4/+a7fh7N4F1IrPpJIMGb+; slave_sid=ODM1VnZyYXBLYXc1SHZzTXdqSXFnMHEzclNpUjBUc3E5cDVEdWlzUXNQR0ZkdnM5Vko1MGFNd1pyV3N0T01pQTV0UGNyQ3NKeFRmUWVfOUVydTA0Z1NoYkR4SW9ZaGNJOXJ1N2JxOUhjT1lENWp3b09PRDFsdkpZV3d2UWhrd0tUNzJhRUd0N053UnFjTnBl; slave_user=gh_a073ba609c88; xid=fff2f9c2f1b389804e4991969ea7256d"
	token = "1937548426"
	gzhListMessage = []
	for gzh in gzhList:
		print(gzh['title'])
		queryKey = gzh['title']
		url = "https://mp.weixin.qq.com/cgi-bin/searchbiz?lang=zh_CN&action=search_biz&begin=0&count=5&query=%s&token=%s&f=json"%(queryKey, token)
		rst = getGzhJson(url, cookie)
		gzhMessage = rst['list'][0]
		# print(jsonify(jsonList))
		print(gzhMessage)
		gzhListMessage.append(gzhMessage)
	print(gzhListMessage)
	return gzhListMessage


# 获取文章列表
def articleList():
	# gzhListMessage = bizList()
	gzhListMessage = [
		{"title": "混知", "fakeid": "MjM5Mjg3MTIzMQ==", "num": "8"},
		{"title": "量子位", "fakeid": "MzIzNjc1NzUzMw==", "num": "7"},
		{"title": "虎嗅APP", "fakeid": "MTQzMjE1NjQwMQ==", "num": "5"},
		# {"title": "占豪", "fakeid": "MzUxNjUxMTg3OA==", "num": "5"},
		# {"title": "差评", "fakeid": "MzA5NDc1NzQ4MA==", "num": "4"},

		{"title": "科技每日推送", "fakeid": "MjM5NzAwNzMyMA==", "num": "4"},
		{"title": "华尔街见闻", "fakeid": "MjM5NzAwMzU0MA==", "num": "3"},
		{"title": "央视财经", "fakeid": "MjM5NzQ5MTkyMA==", "num": "3"},
		{"title": "牛弹琴", "fakeid": "MzA5OTk4NDYwMw==", "num": "2"},
		{"title": "罗列思维", "fakeid": "MzI3Mzg3NDQ2Mw==", "num": "2"},

		{"title": "机器之心", "fakeid": "MzA3MzI4MjgzMw==", "num": "2"},
		{"title": "36氪", "fakeid": "MzI2NDk5NzA0Mw==", "num": "2"},
		{"title": "洞见", "fakeid": "MjM5MDc0NTY2OA==", "num": "2"},

		{"title": "云头条", "fakeid": "MzI4OTc4MzI5OA==", "num": "1"},
		{"title": "数局", "fakeid": "MzU2MjcxNzkwNw==", "num": "1"},
		{"title": "地球知识局", "fakeid": "MzkyNzIwODI3OA==", "num": "1"},
		{"title": "新智元", "fakeid": "MzI3MTA0MTk1MA==", "num": "1"},
		{"title": "一点财经", "fakeid": "MzUxNDcwNjIwNQ==", "num": "1"},

		# {"title": "科技兽", "fakeid": "MzUzNDY2NDc0OQ==", "num": "1"},
		# {"title": "华尔街见闻", "fakeid": "MjM5NzAwMzU0MA==", "num": "1"},
		# {"title": "第一财经", "fakeid": "MjM5MTM3NTMwNA==", "num": "1"},
		# {"title": "雪球", "fakeid": "MzA5MjE3ODgzNA==", "num": "1"},
		# {"title": "AI科技评论", "fakeid": "MzA5ODEzMjIyMA==", "num": "1"},

		# {"title": "晚点LatePost", "fakeid": "", "num" : "1" },
		# {"title": "酷玩实验室", "fakeid": "", "num": "1"},
		# {"title": "泽平宏观", "fakeid": "", "num": "1"},
		# {"title": "远方青木", "fakeid": "", "num": "1"},
		#

		# {"title": "知识星球精选", "fakeid": "", "num": "1"},
		# {"title": "游戏葡萄", "fakeid": "", "num": "1"},
		#
		# {"title": "电手", "fakeid": "", "num": "1"},
		# {"title": "品玩", "fakeid": "", "num": "1"},
		# {"title": "CSDN", "fakeid": "", "num": "1"},
		#
		# {"title": "牲产队", "fakeid": "", "num": "1"},
		# {"title": "芯智讯", "fakeid": "", "num": "1"},
		# {"title": "郎club", "fakeid": "", "num": "1"},

		# {"title": "新零售", "fakeid": "", "num": "1"},
		# {"title": "环球科学", "fakeid": "", "num": "1"},
		# {"title": "中国基金报", "fakeid": "", "num": "1"},
		# {"title": "IT之家", "fakeid": "", "num": "1"},
		# {"title": "猿大侠", "fakeid": "", "num": "1"},

		# {"title": "大佬动向", "fakeid": "", "num": "1"},
		# {"title": "哎咆科技", "fakeid": "", "num": "1"},
		# {"title": "掌链", "fakeid": "", "num": "1"},
		#
		# {"title": "数字孪生城市", "fakeid": "", "num": "1"},
		# {"title": "环球零碳", "fakeid": "", "num": "1"},
		# {"title": "刘润", "fakeid": "", "num": "1"},
		# {"title": "中国科学报", "fakeid": "", "num": "1"},
		# {"title": "科技狐", "fakeid": "", "num": "1"},
		#
		# {"title": "科技美学", "fakeid": "", "num": "1"},
		# {"title": "科研圈", "fakeid": "", "num": "1"},
		# {"title": "果壳", "fakeid": "", "num": "1"},
		# {"title": "躺倒鸭", "fakeid": "", "num": "1"},
		# {"title": "靠山屯闲话", "fakeid": "", "num": "1"},
		#
		# {"title": "爱范儿", "fakeid": "", "num": "1"},
		# {"title": "笔记侠", "fakeid": "", "num": "1"},

	]
	gzhArticleList = []
	cookie = "appmsglist_action_3089078790=card; ua_id=RiaKq2DWeI8pa92xAAAAACOb44d-yM_2meLYVplVmHo=; wxuin=78273871681937; mm_lang=zh_CN; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; cert=semsXcQewJVYHJygpjMu7lkFg3H2dvDx; _t_qbtool_uid=aaaa11dtatg4nlebca5du8ve4ig588cb; _ga=GA1.1.1097700864.1678329752; _ga_QL0HTHVWN7=GS1.1.1678334114.2.0.1678334114.0.0.0; pgv_info=ssid=s4846925475; pgv_pvid=1009145900; ts_uid=3783642033; pac_uid=0_55f106c61eeae; RK=/l+kyqSJWO; ptcz=dffcd32f040bac5b09e84e15a363e4bccaa96374e78fa1cd5e502cfbeec660fc; tvfe_boss_uuid=f486e1ad815eb9d8; vversion_name=8.2.95; video_omgid=b6ba72e8c5fa7503; mmad_session=ae62d6499c344c02cf5d37550bc9e4107baa8a0e3ee0079c75c865740de9a222d321c39da7a6b5a07f512cb2adf8a8e49d26b47b303dace0a349054f88201691142d42a7da0518859105b37addde4a94cb2486b5b19196276b709666deff698f11de1c56c245721266e7088080fefde3; uin=o1103555478; skey=@drGAZlWD8; sig=h018bfaaf9c11db8bd724141ea7ab7a40a218f79459dd3e204149240af18a751504e52002eac2ff8f28; noticeLoginFlag=1; uuid=e83cc724d8df496b1b945c91628be10e; bizuin=3089078790; ticket=855708e79ae6a6adefb1b629cbab316acb3163fd; ticket_id=gh_a073ba609c88; slave_bizuin=3089078790; remember_acct=1103555478%40qq.com; rand_info=CAESIHxsMZLsB8TInpgIEw9IlT0eutRcGNyzdBIkzb2qbgx6; data_bizuin=3089078790; data_ticket=W+asBPVuszJUBvCA7KDd7M4JaUa9lf71w6gV1eet+BnIjILaAvgy0eATjWHLhP4O; slave_sid=NFBvTUtQVm1RaUIzdkIwelR0TmtBcDFMZHJZZ215c0N0YlV1UnJrVXBQY19lVVV6cHJSSXRIRTIwV05LcEtvUXhXS2Z1RV9WcHVBcjc1bTI0cUJUcFkyU3I4cnZBaGZ4YjlJRUZVSHY1N3U1Rlp6R3lvRDNxejk1NGpWdXZxeXpFeTg4WEd3aTdUQ0FYQ0N3; slave_user=gh_a073ba609c88; xid=967d5394007921197b3e8c736f75854e; openid2ticket_oBpofuF_qFGES7wjwtT86jLLrcXs=kp/2n2AUVtIUxOGwclaGBUR+wWNuMyjmd5bdPcIU3bk=; _clck=3089078790|1|fbs|0; _clsk=19r7nln|1684679359373|4|1|mp.weixin.qq.com/weheat-agent/payload/record"
	token = "867320945"
	for gzh in gzhListMessage:
		fakeid = gzh["fakeid"]
		# fakeid = "MzIxNTAzNzU0Ng=="
		query = ""
		url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=1&fakeid=%s&type=9&query=%s&token=%s&lang=zh_CN&f=json"%(fakeid, query, token)
		jsonList = getGzhJson(url, cookie)['app_msg_list']
		# print(jsonList[0])
		if len(jsonList) > 0:
			article = jsonList[0]
			print("name: " + gzh['title'] + " title: " + article['title'])
			print(article['link'])
		# 判断是不是前天发布的新内容
		# 今天日期
		# today = datetime.date.today()
		# 昨天时间
		# yesterday = today - datetime.timedelta(days=1)
		# 昨天开始时间戳
		# yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
		# 昨天结束时间戳
		# yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
		# if yesterday_start_time < article['create_time']:
		# 	print("name: "+ gzh['title'] + " title: " + article['title'])
		# 	print(article['link'])
		# 	gzhArticleList.append(article)
		# print("前天发布的所有文章列表： " + str(gzhArticleList))




if __name__ == '__main__':
	 # app.run(host='localhost', port = 10845)
	 # print("ffg")
	 # bizList()
	 articleList()



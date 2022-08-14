import json
import time
import requests
from requests import *
from datetime import datetime
from config import *
from tiktok_module import downloader

api = "https://api.telegram.org/bot" + token_bot
update_id = 0

def SendVideo(userid,msgid):
	tg_url = api + "/sendvideo"
	data = {
		"chat_id":userid,
		"caption":"<b>تم تنزْيلُِ عٍبَرٍ :</b> @SEL_TK_BOT \n\n<b>𝚂𝙴𝙻𝚅𝙴𝚁 - 𝙳𝙴𝚅</b> : <i>𖥳𖥳𖥳 @SELVER7 𖥳𖥳𖥳</i>\n<b>𝙲𝙷</b> : <i>𖥳𖥳𖥳 @M_GO_17q 𖥳𖥳𖥳</i>",
		"parse_mode":"html",
		"reply_to_message_id":msgid,
		"reply_markup":json.dumps({
			"inline_keyboard":[
				[
					{
						"text":"𝚂𝙴𝙻𝚅𝙴𝚁 - 𝙳𝙴𝚅 <3",
						"url":"https://t.me/SELVER7"
					}
				]
			]
		})
	}
	res = post(
		tg_url,
		data=data,
		files={
			"video":open("video.mp4","rb")
		}
	)

def SendMsg(userid,text,msgid):
	tg_url = api + "/sendmessage"
	post(
		tg_url,
		json={
			"chat_id":userid,
			"text":text,
			"parse_mode":"html",
			"reply_to_message_id":msgid
		}
	)

def get_time(tt):
	ttime = datetime.fromtimestamp(tt)
	return f"{ttime.hour}-{ttime.minute}-{ttime.second}-{ttime.day}-{ttime.month}-{ttime.year}"

def Bot(update):
	try:
		global last_use
		userid = update['message']['chat']['id']
		meseg = update['message']['text']
		msgid = update['message']['message_id']
		timee = update['message']['date']
		dl = downloader.tiktok_downloader()
		if update['message']['chat']['type'] != "private":
			SendMsg(
				userid,
				"آلُِبَوُت يعٍملُِ فُقٌطُ فُي آلُِدِرٍدِشُة آلُِخـآصة!",
				msgid
			)
			return
		first_name = update['message']['chat']['first_name']
		print(f"{get_time(timee)}-> {userid} - {first_name} -> {meseg}")
		if meseg.startswith('/start'):
			SendMsg(
				userid,
				"<b>آهـلُِآبَڪ فُي بَوُت تحٍميلُِ فُيدِيوُهـآت من تيڪ توُڪ</b>\n\n<b>ڪيفُ تستخـدِم هـذَآ بَوُت ؟ </b>:\n<i>فُقٌطُ آرٍسلُِ رٍآبَطُ فُيدِيوُ من تيڪ توُڪ آلُِي هـذَآ بَوُت </i>!!\n",
				msgid
			)
		elif "tiktok.com" in meseg and "https://" in meseg :
			getvid = dl.musicaldown(url=meseg,output_name="video.mp4")
			if getvid == False:
				SendMsg(
					userid,
					"<i>فُشُلُِ فُي تحٍميلُِ فُيدِيوُ</i>\n\n<i>حاول مجددا لا حقا</i>",
					msgid
				)
				return
			elif getvid == "private/remove":
				SendMsg(
					userid,
					"<i>فُشُلُِ فُي تحٍميلُِ فُيدِيوُ</i>\n\n<i>ڪآن آلُِفُيدِيوُ خـآصًآ أوُ تمت إزْآلُِته</i>",
					msgid
				)
			elif getvid == "file size is to large":
				SendMsg(
					userid,
					"<i>فُشُلُِ فُي تحٍميلُِ فُيدِيوُ</i>\n\n<i>حٍجٍم فُيدِيوُ ڪبَيرٍ </i>",
					msgid
				)
			else:
				SendVideo(
					userid,
					msgid
				)
		elif "/help" in meseg:
			SendMsg(
				userid,
				"ڪيفُ تستخـدِم هـذَآ بَوُت ؟ :\فُقٌطُ آرٍسلُِ رٍآبَطُ فُيدِيوُ من تيڪ توُڪ آلُِي هـذَآ بَوُت ! ",
				msgid
			)
		elif meseg.startswith("/donation"):
			SendMsg(
				userid,
				"Support me on\n\nko-fi (EN): https://ko-fi.com/fowawaztruffle\nsaweria (ID): https://saweria.co/fowawaztruffle\ntrakteerid (ID): https://trakteer.id/fowawaz\nQRIS (EWALLET,BANK): https://s.id/nusantara-qr",
				msgid
			)
	except KeyError:
		return

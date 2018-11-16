import os

from clicktocall.app import app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    if port == 8080:
        app.debug = True
    app.run(host='0.0.0.0', port=port)
# account_sid = 'ACb78bda6471d6cb3bf521a5520990ca7a'
# auth_token = 'f83cbe3c67248ab5a0c4c1acb90a56a1'
# client = Client(account_sid, auth_token)
# # 	call = client.calls.create(
# # 						url='http://demo.twilio.com/docs/voice.xml',
# # 						to='+919770445436',
# # 						from_='+18446523945'
# # 					)
# # 	print(call.sid)
# # 	return call.sid
# 	#+18446523945
# f __name__ == "__main__":
# 	call()
# 	print("call is in progress")
# 	port = int(os.environ.get("PORT", 8080))
# 	app.run(host='0.0.0.0', port=port)i
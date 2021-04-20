import base64

cipher='Y3liZXJwZWFjZXtXZWxjb21lX3RvX25ld19Xb3JsZCF9'
plainer= base64.b64decode(cipher)
print(str(plainer,'utf-8'))

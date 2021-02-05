## 3. Converse API > Debug API

Send requests to [Debug API](https://botpress.com/docs/channels/converse).  
Run `HTTP` command to check confidence one by one as follows if you have [HTTPie](https://httpie.io/) in your environment.

```bash
$ http POST http://localhost:5000/api/v1/bots/sample-bot-1/converse/oasist/secured include==state,suggestions type=text text=GitHub 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImlzaGlkYUByZWxpYS1kaWdpdGFsLmNvbSIsInN0cmF0ZWd5IjoiZGVmYXVsdCIsImlzU3VwZXJBZG1pbiI6dHJ1ZSwiaWF0IjoxNjAzMTY3MzA3LCJleHAiOjE2MDMxODg5MDcsImF1ZCI6ImNvbGxhYm9yYXRvcnMifQ.yML7o_n-wRY6dqNXVKOsO42zCkzAjSepfNAhUQH4RfU'
```

```JSON
{
    "responses": [
        {
            "type": "typing",
            "value": true
        },
        {
            "type": "text",
            "text": "ソフトウェア開発のプラットフォームであり、ソースコードをホスティングする。コードのバージョン管理システムにはGitを使用します。",
            "collectFeedback": true
        }
    ],
    "suggestions": [
        {
            "confidence": 0.851,
            "payloads": [
                {
                    "type": "typing",
                    "value": true
                },
                {
                    "type": "text",
                    "text": "ソフトウェア開発のプラットフォームであり、ソースコードをホスティングする。コードのバージョン管理システムにはGitを使用します。",
                    "collectFeedback": true
                }
            ],
            "source": "qna",
            "sourceDetails": "__qna__1oqmnlzvdx_github",
            "decision": {
                "status": "elected",
                "reason": "best remaining suggestion available"
            }
        },
        {
            "confidence": 0.149,
            "payloads": [
                {
                    "type": "typing",
                    "value": true
                },
                {
                    "type": "text",
                    "text": "「設定」→「アカウント」→「アカウント削除」より削除してください。",
                    "collectFeedback": true
                }
            ],
            "source": "qna",
            "sourceDetails": "__qna__ij4guuwsfr_github",
            "decision": {
                "status": "dropped",
                "reason": "confidence lower than 0.5"
            }
        }
    ],
    "state": {
        "__stacktrace": [],
        "user": {
            "0": "{",
            "1": "}"
        },
        "context": {},
        "session": {
            "lastMessages": [
                {
                    "eventId": "160317710111814000",
                    "replyDate": "2020-10-20T06:58:21.676Z",
                    "replySource": "qna __qna__nvki9hmrv4_prime_video",
                    "incomingPreview": "Prime Videoはタダで使えるのか",
                    "replyConfidence": 0.715,
                    "replyPreview": {
                        "type": "text",
                        "text": "月額500円、年額4900円の有料サービスです。",
                        "collectFeedback": true
                    }
                },
                {
                    "eventId": "160317710193784160",
                    "replyDate": "2020-10-20T06:58:22.454Z",
                    "replySource": "qna __qna__1d01hra1au_",
                    "incomingPreview": "メールアドレスはどこからどうやって変更できるか",
                    "replyConfidence": 0.608,
                    "replyPreview": {
                        "type": "text",
                        "text": "アカウント情報のページより編集できます。",
                        "collectFeedback": true
                    }
                },
                {
                    "eventId": "160317710271434020",
                    "replyDate": "2020-10-20T06:58:23.299Z",
                    "replySource": "qna __qna__7ao81uivks_prime_video",
                    "incomingPreview": "Prime Videoを解約したんだけど",
                    "replyConfidence": 0.655,
                    "replyPreview": {
                        "type": "text",
                        "text": "アカウント情報のページより解約していただけます。Amazon Primeを解約すると、ショッピングの配達日指定、Amazon Music、Amazon Kindle等のサービスもご利用いただけなくなります。",
                        "collectFeedback": true
                    }
                },
                {
                    "eventId": "160317792209616770",
                    "replyDate": "2020-10-20T07:12:02.908Z",
                    "replySource": "qna __qna__1oqmnlzvdx_github",
                    "incomingPreview": "GitHub",
                    "replyConfidence": 0.851,
                    "replyPreview": {
                        "type": "text",
                        "text": "ソフトウェア開発のプラットフォームであり、ソースコードをホスティングする。コードのバージョン管理システムにはGitを使用します。",
                        "collectFeedback": true
                    }
                },
                {
                    "eventId": "160317793123118940",
                    "replyDate": "2020-10-20T07:12:12.003Z",
                    "replySource": "qna __qna__1oqmnlzvdx_github",
                    "incomingPreview": "GitHub",
                    "replyConfidence": 0.851,
                    "replyPreview": {
                        "type": "text",
                        "text": "ソフトウェア開発のプラットフォームであり、ソースコードをホスティングする。コードのバージョン管理システムにはGitを使用します。",
                        "collectFeedback": true
                    }
                }
            ],
            "workflows": {},
            "slots": {}
        },
        "temp": {}
    }
}
```

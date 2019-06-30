import json
import dialog

#Test return with chart format.
test_ret = {
	'radarCharts': [
		{
			'title': "Trends",
			'data': [
				{ 'word': "Blockchain", 'A': 150, 'fullMark': 150 },
				{ 'word': "Cyrpto", 'A': 150, 'fullMark': 150 },
				{ 'word': "IOT", 'A': 86, 'fullMark': 150 },
				{ 'word': "Security", 'A': 99, 'fullMark': 150 },
				{ 'word': "Automation", 'A': 85, 'fullMark': 150 }
			]
		}
	],

	'ratioBarCharts': [
		{
			'title': "I vs We",
			'data': [{ 'label': "I/Me", 'percent': 10, 'val': 5 }, { 'label': "We/Us", 'percent': 90, 'val': 45 }]
		},
		{
			'title': "Postive vs Negative",
			'data': [{ 'label': "Positive", 'percent': 40, 'val': 100 }, { 'label': "Negative", 'percent': 60, 'val': 400 }]
		}
	],
	'textCharts': [
		{
			'title': "Words similar to Team",
			'data': "7232 Mentions"
		},
		{
			'title': "Questions Asked",
			'data': "7 Questions"
		}
	]
}


def main(request):

    request_json = request.get_json()
    
    output = json.dumps(test_ret)
    
    if request.args and 'ID' in request.args:
        return request.args.get('ID')
    elif request_json and 'text' in request_json and 'profile' in request_json:
        output = dialog.get_metrics(request_json['profile'], request_json['text'])
        return (json.dumps(output))
    else:
        return (output)

if __name__ == '__main__':  
    main()
import requests, json
import pprint


# top 10 websites in US, (source: alexa.com)
seed_urls = ["google.com", "facebook.com", "amazon.com", "youtube.com", "yahoo.com", "wikipedia.org", "ebay.com",
             "twitter.com", "reddit.com", "go.com"]


# get WebAim accessiblity issues for seed urls
def get_errors():
    api_key = ''
    errors = {}
    errors_item_count = {}
    error_item_description = {}

    alerts = {}
    alerts_item_count = {}
    alerts_item_description = {}

    feature_issues = {}
    feature_item_count = {}
    feature_item_description = {}

    structural_issues = {}
    structural_item_count = {}
    structural_item_description = {}

    html5_issues = {}
    html5_item_count = {}
    html5_item_description = {}

    contrast_issues = {}
    contrast_item_count = {}
    contrast_item_description = {}

    for i in seed_urls:
        result = requests.get('http://wave.webaim.org/api/request?key='+api_key+'&url='+i+'&reporttype=2')
        result_json = json.loads(result.text)
        print "Credits remaining: ", result_json['statistics']['creditsremaining']

        result_categories = result_json['categories']
        for category in result_categories:
            if category == 'error':
                errors[i] = result_categories[category]['count']

                # get individual item count
                if result_categories[category]['count'] > 0:
                    error_item = result_categories[category]['items']

                    # get the count of each item
                    for item in error_item:
                        if item in errors_item_count:
                            cur_count = errors_item_count[item]
                            new_count = cur_count + error_item[item]['count']
                            errors_item_count[item] = new_count
                        else:
                            errors_item_count[item] = error_item[item]['count']
                            error_item_description[item] = error_item[item]['description']

            elif category == 'alert':
                alerts[i] = result_categories[category]['count']

                # get the count of each item
                if result_categories[category]['count'] > 0:
                    alert_item = result_categories[category]['items']
                    for item in alert_item:
                        if item in alerts_item_count:
                            cur_count = alerts_item_count[item]
                            new_count = cur_count + alert_item[item]['count']
                            alerts_item_count[item] = new_count
                        else:
                            alerts_item_count[item] = alert_item[item]['count']
                            alerts_item_description[item] = alert_item[item]['description']

            elif category == 'feature':
                feature_issues[i] = result_categories[category]['count']

                # get the count of each item
                if result_categories[category]['count'] > 0:
                    feature_item = result_categories[category]['items']
                    for item in feature_item:
                        if item in feature_item_count:
                            cur_count = feature_item_count[item]
                            new_count = cur_count + feature_item[item]['count']
                            feature_item_count[item] = new_count
                        else:
                            feature_item_count[item] = feature_item[item]['count']
                            feature_item_description[item] = feature_item[item]['description']

            elif category == 'structural':
                structural_issues[i] = result_categories[category]['count']

                # get the count of each item
                if result_categories[category]['count'] > 0:
                    structural_item = result_categories[category]['items']
                    for item in structural_item:
                        if item in structural_item_count:
                            cur_count = structural_item_count[item]
                            new_count = cur_count + structural_item[item]['count']
                            structural_item_count[item] = new_count
                        else:
                            structural_item_count[item] = structural_item[item]['count']
                            structural_item_description[item] = structural_item[item]['description']

            elif category == 'html5':
                html5_issues[i] = result_categories[category]['count']

                # get the count of each item
                if result_categories[category]['count'] > 0:
                    html5_item = result_categories[category]['items']
                    for item in html5_item:
                        if item in html5_item_count:
                            cur_count = html5_item_count[item]
                            new_count = cur_count + html5_item[item]['count']
                            html5_item_count[item] = new_count
                        else:
                            html5_item_count[item] = html5_item[item]['count']
                            html5_item_description[item] = html5_item[item]['description']

            elif category == 'contrast':
                contrast_issues[i] = result_categories[category]['count']

                # get the count of each item
                if result_categories[category]['count'] > 0:
                    contrast_item = result_categories[category]['items']
                    for item in contrast_item:
                        if item in contrast_item_count:
                            cur_count = contrast_item_count[item]
                            new_count = cur_count + contrast_item[item]['count']
                            contrast_item_count[item] = new_count
                        else:
                            contrast_item_count[item] = contrast_item[item]['count']
                            contrast_item_description[item] = contrast_item[item]['description']

    overall_error_data = {
        'error_counts': errors,
        'error_item_counts': errors_item_count,
        'error_item_description': error_item_description
    }

    # write json to respective files for data analysis
    with open('json_data/error_count_overall.json', 'w') as error_file:
        error_file.write(json.dumps(overall_error_data))

    overall_alert_data = {
        'alert_counts': alerts,
        'alert_item_counts': alerts_item_count,
        'alert_item_description': alerts_item_description
    }

    # write json to respective files for data analysis
    with open('json_data/alert_count_overall.json', 'w') as alert_file:
        alert_file.write(json.dumps(overall_alert_data))

    overall_feature_data = {
        'feature_counts': feature_issues,
        'feature_item_counts': feature_item_count,
        'feature_item_description': feature_item_description
    }

    # write json to respective files for data analysis
    with open('json_data/feature_count_overall.json', 'w') as feature_file:
        feature_file.write(json.dumps(overall_feature_data))

    overall_structural_data = {
        'structural_counts': structural_issues,
        'structural_item_counts': structural_item_count,
        'structural_item_description': structural_item_description
    }

    # write json to respective files for data analysis
    with open('json_data/structural_count_overall.json', 'w') as structural_file:
        structural_file.write(json.dumps(overall_structural_data))

    overall_html5_data = {
        'html5_counts': html5_issues,
        'html5_item_counts': html5_item_count,
        'html5_item_description': html5_item_description
    }

    # write json to respective files for data analysis
    with open('json_data/html5_count_overall.json', 'w') as html5_file:
        html5_file.write(json.dumps(overall_html5_data))

    overall_contrast_data = {
        'contrast_counts': contrast_issues,
        'contrast_item_counts': contrast_item_count,
        'contrast_item_description': contrast_item_description
    }

    # write json to respective files for data analysis
    with open('json_data/contrast_count_overall.json', 'w') as contrast_file:
        contrast_file.write(json.dumps(overall_contrast_data))

    # create a master json with all the category data
    master_data = {
        'errors': overall_error_data,
        'alerts': overall_alert_data,
        'features': overall_feature_data,
        'structural': overall_structural_data,
        'html5': overall_html5_data,
        'contrast': overall_contrast_data
    }

    with open('json_data/total_accessiblity_issues.json', 'w') as accessibility_file:
        accessibility_file.write(json.dumps(master_data))


def read_error_data():
    with open('json_data/error_count_overall.json') as data_file:
        data = json.load(data_file)
        del data['error_item_counts']
        del data['error_counts']
        mod_data = data['error_item_description']
        pprint.pprint(mod_data, depth=2)
        with open('error_item_description.json', 'w') as accessibility_file:
            accessibility_file.write(json.dumps(mod_data))

if __name__ == "__main__":
    # get_errors()
    read_error_data()

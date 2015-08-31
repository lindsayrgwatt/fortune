from pyquery import PyQuery as pq

def best_to_work():
    best_to_work_html = pq(filename='best_to_work_for.html')
    targets = best_to_work_html.find('.company-name')

    best_to_work = []
    for target in targets:
        best_to_work.append(target.text.lower())

    return best_to_work

def most_admired():
    most_admired_html = pq(filename='top_50_most_admired.html')
    targets = most_admired_html.find('.article-permalink')

    most_admired = []
    for target in targets:
        most_admired.append(target.text.lower())

    top_50 = most_admired[0:50]

    return top_50

def compare_lists():
    best_to_work_companies = best_to_work()
    most_admired_companies = most_admired()

    overlap = []
    for company in best_to_work_companies:
        if company in most_admired_companies:
            overlap.append(company)

    print overlap

if __name__ == '__main__':
    compare_lists()

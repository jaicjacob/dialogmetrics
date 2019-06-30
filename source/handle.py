from nltk.classify import SklearnClassifier
import pickle
import sentiment as senti

################################################################################
# COMMON FUNCTIONS
################################################################################
#safe division
def safe_div(x, y):
    rtn = 0
    if(y != 0):
        rtn = x/y
    return(rtn)

#return the sorted word list according to the key and style (if 1:decsending)
def word_sort(style, token, word_list):
    return(sorted(word_list, key = lambda i: i[token], reverse = style))


#returns the number of iterations of a given word
def word_cnt(word, word_list):
    count = 0
    for p in word_list:
        if p['word'] == word:
            count = p['count']
            break
    return(count)


#returns the number of iterations of a given word type
def word_type(token, word_list):
    counter = 0
    for p in word_list:
        if p['type'] == token:
            counter = counter + p['count']
    return(counter)

#returns the frequency of a given word
def word_freq(word, word_list):
    total_words = 0
    for p in word_list:
        total_words = total_words + p['count']
        if p['word'] == word:
            counter = p['count']
    return(counter/total_words)


#returns the top words of a style argument
def top_word(style, number):
    counter = 0
    out_dict = {}
    out_list = []
    inp_list = word_sort(1,'count')
    for p in inp_list:
        if p['type'] == style:
            out_dict['word'] = p['word']
            out_dict['count'] = p['count']
            out_list.append(out_dict.copy())
            counter = counter + 1
        if counter >= number:
            return out_list

################################################################################
# CUSTOM FUNCTIONS
################################################################################

#iterative words: try, create, make, sketch, plan, build, think, discuss, optimize
def iterative_words(word_list):
    
    output = {}
    data = {}
    counter = []
    checker = ['try', 'create', 'make', 'sketch', 'plan', 'build', 'think', 'discuss', 'optimize']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter.append(word_cnt(checker[idx], word_list))
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Iterative Words"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#learning words: new, check, find, research, analyse, learn
def learning_words(word_list):
    
    output = {}
    data = {}
    counter = {}
    checker = ['new', 'check', 'find', 'research', 'analyse', 'learn']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Learning Words"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#creative words: inspire, inspiration, practices, design, reference
def creative_words(word_list):
    
    output = {}
    data = {}
    counter = {}
    checker = ['inspire', 'inspiration', 'practice', 'design', 'reference']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Creative Words"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#curiosity index: asking questions
def curiosity_idx(word_list):
    
    output = {}

    count = word_type('WDT', word_list)
    count = count + word_type('WP', word_list)
    count = count + word_type('WRB', word_list)

    output['title'] = "Curiosity Index"
    output['data'] = count

    return output

#timeliness words: deadline, timeline, time, efficency, focus
def timeliness_check(word_list):
    
    output = {}
    data = {}
    counter = {}
    checker = ['deadline', 'timeline', 'time', 'efficency', 'focus']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Timeliness"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#consistancy words: always, every, each
def consistancy_check(word_list):
    
    output = {}
    data = {}
    counter = {}
    checker = ['always', 'every', 'each']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Consistancy"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

def sentiment_analysis(word_list):
    neg_cnt = 0
    pos_cnt = 0
    output = {}

    classifier_f = open(".\Include\sentiment.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()

    for obj in word_list: 
        res =  classifier.classify(senti.extract_features(obj['word']))
        if(res == 'Negative'): 
            neg_cnt = neg_cnt + 1
    # for obj in word_list: 
    #     res =  classifier.classify(senti.extract_features(obj['word']))
    #     if(res == 'Positive'): 
    #         pos_cnt = pos_cnt + 1

    output['title'] = "Negative Index"
    output['data'] = 100 * (neg_cnt/len(word_list))

    return(output)

#lead words: inspire, support, help, team, energise, believe, motivate, allocate
def lead_phrases(word_list):
        
    output = {}
    data = {}
    counter = {}
    checker = ['inspire', 'support', 'help', 'team', 'energise', 'believe', 'motivate', 'allocate']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Consistancy"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#motivation words: can, will, would
def motivation_check(word_list):
        
    output = {}
    data = {}
    counter = {}
    checker = ['can', 'will', 'would']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Consistancy"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#manager words: inspire, support, help, team, energise, believe
def manager_phrases(word_list):
        
    output = {}
    data = {}
    counter = {}
    checker = ['inspire', 'support', 'help', 'team', 'energise', 'believe']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Manager Phrases"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#Comparision between I and we
def i_vs_we(word_list):
    
    output = {}
    data = []
    temp = {}
    temp1 = {}
    
    i = word_cnt('i', word_list)
    me = word_cnt('me', word_list)
    we = word_cnt('we', word_list)
    us = word_cnt('us', word_list)
    
    total_individual = i + me
    total_group = we + us
    total = total_individual + total_group

    temp['label'] = "I/Me"
    temp['percent'] = 100 * safe_div(total_individual,total)
    temp['val'] = total_individual
    data = [temp]
    temp1['label'] = "We/Us"
    temp1['percent'] = 100 * safe_div(total_group,total)
    temp1['val'] = total_group
    data.append(temp1)


    output['title'] = "I/Me vs We/Us"
    output['data'] = data

    return(output)

#Comparision between past and present
def past_vs_present(word_list):
    
    output = {}
    data = []
    temp = {}
    temp1 = {}
        
    past = word_type('VBD', word_list)
    past_princ = word_type('VBN', word_list)
    present = word_type('VBP', word_list)
    present_princ = word_type('VBG', word_list)
    
    total_past = past + past_princ
    total_present = present + present_princ
    total = total_past + total_present

    temp['label'] = "Past"
    temp['percent'] = 100 * safe_div(total_past,total)
    temp['val'] = total_past
    data = [temp]
    temp1['label'] = "Present"
    temp1['percent'] = 100 * safe_div(total_present,total)
    temp1['val'] = total_present
    data.append(temp1)


    output['title'] = "Past vs Present"
    output['data'] = data

    return(output)

#Knowledge sharing: share, teach, educate
def kt_check(word_list):
        
    output = {}
    data = {}
    counter = {}
    checker = ['share', 'teach', 'educate']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Knowledge Sharing"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output

#Group words: team, group, together, us, our, we
def group_words(word_list):
        
    output = {}
    data = {}
    counter = {}
    checker = ['team', 'group', 'together', 'us', 'our', 'we']
    
    #get the count of the checker words
    for idx in range(len(checker)):
        counter[idx] = word_cnt(checker[idx], word_list)
    
    fullMark = max(counter)
    
    #process chart
    output['title'] = "Group Words"
    for idx in range(len(checker)):
        data['word'] = checker[idx]
        data['A'] = counter[idx]
        data['fullMark'] = fullMark
        if('data' in output):
            output['data'].append(data.copy())
        else:
            output['data'] = [data]

    return output
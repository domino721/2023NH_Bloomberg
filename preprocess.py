def remove_enter(article):
    try:
        st = re.sub('\n', '', article)
        st = re.sub('\t', ' ', st)
    except:
        print('error')
        st = None
    return st
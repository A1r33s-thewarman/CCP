ssss = 'kohomadha'

mapper = {
    'a' : '',
    'aa' : 'ා',
    'A' : 'ැ',
    'Aa' : 'ෑ',
    'i' : 'ි',
    'ie' : 'ී',
    'u' : 'ු',
    'uu' : 'ූ',
    'e' : 'ෙ',
    'ei' : 'ේ',
    'o' : 'ො',
    'oe' : 'ෝ',
    'au' : 'ෞ',
    'ra' : '්ර',
    'raa' : '්රා',
    'rA' : '්රැ',
    'rAa' : '්රෑ',
    'ri' : '්රි',
    'rie' : '්රී',
    'ru' : '්රු',
    'ruu' : '්රූ',
    're' : '්රෙ',
    'rei' : '්රේ',
    'ro' : '්රො',
    'roe' : '්රෝ'
}

s2s_mapper = {
    'cc' : 'a',
    '්' : '',
    'ා' : 'aa',
    'ැ' : 'A',
    'ෑ' : 'Aa',
    'ි' : 'i',
    'ී' : 'ie',
    'ු' : 'u',
    'ූ' : 'uu',
    'ෙ' : 'e',
    'ේ' : 'ei',
    'ො' : 'o',
    'ෝ' : 'oe',
    'ෞ' : 'au',
    '්ර' : 'ra',
    '්රා' : 'raa',
    '්රැ' : 'rA',
    '්රෑ' : 'rAa',
    '්රි' : 'ri',
    '්රී' : 'rie',
    '්රු' : 'ru',
    '්රූ' : 'ruu',
    '්රෙ' : 're',
    '්රේ' : 'rei',
    '්රො' : 'ro',
    '්රෝ' : 'roe'
}

common = {
    'අ' : 'a',
    'ඉ' : 'i',
    'එ' : 'e',
    'ඔ' : 'o',
    'උ' : 'u',
    'ක' : 'k',
    'ග' : 'g',
    'ච' : 'ch',
    'ජ' : 'j',
    'ට' : 't',
    'ඩ' : 'd',
    'ත' : 'th',
    'ද' : 'dh',
    'න' : 'n',
    'ප' : 'p',
    'බ' : 'b',
    'ම' : 'm',
    'ය' : 'y',
    'ර' : 'r',
    'ල' : 'l',
    'ව' : 'w',
    'ස' : 's',
    'ණ' : 'n',
    'ළ' : 'l',
    'ඛ' : 'k',
    'ඝ' : 'g',
    'ඡ' : 'ch',
    'ඨ' : 't',
    'ඪ' : 'd',
    'ථ' : 'th',
    'ධ' : 'dh',
    'ඵ' : 'p',
    'භ' : 'b',
    'හ' : 'h',
    'ඹ' : 'b',
    'ශ' : 'sh',
    'ෂ' : 'sh',
    'ෆ' : 'f',
    'ඥ' : 'gn',
    'ඤ' : 'kn',
    'ඣ' : 'q',
    'ං' : 'n'
}



def word_convert(ssss):
    ret = ""
    common_letter = 0
    for i in list(ssss):
        if str(i) in common:
            ret += common[str(i)]
            common_letter = 1
        if common_letter == 1:
            if str(i) in s2s_mapper and ret[-1] == 'a':
                ret = ret[:-1]
                ret += s2s_mapper[str(i)]
            else:
                ret += s2s_mapper['cc']
    return ret


def sentence_conv(sentence):
    conv_sent = ''
    for word in sentence.split():
        conv_sent += word_convert(word)
        conv_sent += ' '
    return conv_sent

print(sentence_conv('කරුණාකරලා'))

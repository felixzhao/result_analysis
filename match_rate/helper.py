import math

def GetDataDict(path):
    infile = open(path, 'r')
    dict = {}
    '''
        Create infile data dict
    '''
    for line in infile.readlines():
        if line.startswith(' '):
            continue
        else:
            w = line.split(':')
            if len(w) > 1:
                t = w[1].split('|')
                v = [x.lstrip(' ').split(' ')[0].strip(' ') for x in t][:-1]
                dict[w[0].strip(' ')] = v
    return dict

def match_rate(match_dict):
    match_count = 0
    match_rate = 0.0
    unk_count = len(match_dict.keys())
    for k in match_dict.keys():
        if k in match_dict[k]:
            match_count += 1
    match_rate = match_count / float(unk_count)
    return (match_rate, match_count, unk_count)
    
def print_result(out_file_match_rate, out_file_match_count, out_file_unk_count, flag, res_bms, res_bl):
    print >> out_file_match_rate, flag,'&', float(res_bms[0]),'&', float(res_bl[0])
    print >> out_file_match_count, flag,'&',res_bms[1],'&',res_bl[1]
    print >> out_file_unk_count, flag,'&',res_bms[2],'&',res_bl[2]
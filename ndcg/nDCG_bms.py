
import sys
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

'''
    nDCG Algorith
'''
def nDCG(key, candidates, idcg):

    list = []

    for cand in candidates:
        if key == cand:
            list.append(1)
        else:
            list.append(0)
            
    dcg_score = list[0]

    for i in xrange(1,len(list)):
        dcg_score += list[i] / math.log(i+1,2)
    ndcg_score = dcg_score / idcg
    return ndcg_score

def sum_ndcg(match_dict, idcg):
    sum = 0.0
    for k in match_dict.keys():
        sum += nDCG(k, match_dict[k], idcg)
    return sum

def higer_count(bms_dict, bl_dict, idcg):
    equal = 0
    bigger = 0
    smaller = 0
    for k in bms_dict.keys():
        bms_score = nDCG(k, bms_dict[k], idcg)
        bl_score = nDCG(k, bl_dict[k], idcg)
        if bms_score > bl_score:
            bigger += 1
        elif bms_score < bl_score:
            smaller += 1
        else:
            equal += 1
    return (bigger, smaller, equal)
        
if __name__ == '__main__':

    beam_width_list = [3,5,10,15,20,25]
    idcg = 1595
    out_file_sum_ndcg = open('out_bms/ana_sum_ndcg.txt','w')
    out_file_ndcg_higer_count = open('out_bms/ana_ndcg_higer_count.txt','w')
    print >> out_file_sum_ndcg, 'Beam Width & Beam Search & Base Line'
    print >> out_file_ndcg_higer_count, 'Beam Width & Beam Search Higher & Base Line Higher & Equals'
    for bw in beam_width_list:
        baseline = '../baseline/baseline_result_33per_' + str(bw) + 'width.txt'
        beamsearch = '../updated/updated_out.bw' + str(bw) + '.ns0.sfw0.type33.txt'
        baseline_dict = GetDataDict(baseline)
        beamsearch_dict = GetDataDict(beamsearch)
        '''
            sum ndcg
        '''
        res_sum_bl = sum_ndcg(baseline_dict, idcg)
        res_sum_bms = sum_ndcg(beamsearch_dict, idcg)
        print >> out_file_sum_ndcg, bw,'&', float(res_sum_bms),'&', float(res_sum_bl)
        '''
            higher count
        '''
        res_higer_count = higer_count(beamsearch_dict, baseline_dict, idcg)
        print >> out_file_ndcg_higer_count, bw,'&', res_higer_count[0],'&', res_higer_count[1],'&',res_higer_count[2] 
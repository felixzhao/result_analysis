from helper import *
     
if __name__ == '__main__':
    beam_width_list = [3,5,10,15,20,25]
    out_file_match_rate = open('out_match_rate_with_bw/ana_match_rate.txt','w')
    out_file_match_count = open('out_match_rate_with_bw/ana_match_count.txt','w')
    out_file_unk_count = open('out_match_rate_with_bw/ana_unk_count.txt','w')
    print >> out_file_match_rate, 'Beam Width & Beam Search & Base Line'
    print >> out_file_match_count, 'Beam Width & Beam Search & Base Line'
    print >> out_file_unk_count, 'Beam Width & Beam Search & Base Line'
    for bw in beam_width_list:
        beamsearch = '../updated/updated_out.bw' + str(bw) + '.ns0.sfw0.type33.txt'
        baseline = '../baseline/baseline_result_33per_' + str(bw) + 'width.txt'
        beamsearch_dict = GetDataDict(beamsearch)
        baseline_dict = GetDataDict(baseline)
        res_bms = match_rate(beamsearch_dict)
        res_bl = match_rate(baseline_dict)
        '''
        print result
        '''
        print_result(out_file_match_rate, out_file_match_count, out_file_unk_count, bw, res_bms, res_bl)
from helper import *
        
if __name__ == '__main__':
    bw = '20'
    noise_size = ['#',3,2,1]
    out_file_match_rate = open('out_match_rate_with_ns/ana_match_rate.txt','w')
    out_file_match_count = open('out_match_rate_with_ns/ana_match_count.txt','w')
    out_file_unk_count = open('out_match_rate_with_ns/ana_unk_count.txt','w')
    print >> out_file_match_rate, 'Noise Size & Beam Search & Base Line'
    print >> out_file_match_count, 'Noise Size & Beam Search & Base Line'
    print >> out_file_unk_count, 'Noise Size & Beam Search & Base Line'
    for ns in noise_size:
        if ns == '#':
            beamsearch = '../updated/updated_out.bw'+ bw +'.ns0.sfw0.type33.txt'
            baseline = '../baseline/baseline_result_33per_10width.txt'
        else:
            beamsearch = '../updated/updated_out.bw'+ bw +'.ns' + str(ns) + '.sfw10.type33.txt'
            baseline = '../baseline/baseline_result_33per_'+ bw +'width.txt'
        beamsearch_dict = GetDataDict(beamsearch)
        baseline_dict = GetDataDict(baseline)
        res_bms = match_rate(beamsearch_dict)
        res_bl = match_rate(baseline_dict)
        '''
        print result
        '''
        print_result(out_file_match_rate, out_file_match_count, out_file_unk_count, ns, res_bms, res_bl)
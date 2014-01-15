
import sys

beam_width_list = [3,5,10,15,20,25]

for bw in beam_width_list:
  infile_path = 'BeamSearch/out.bw' + str(bw) + '.ns0.sfw0.type33.txt'
  word_map_path = 'source/src-33percent/word-map.txt'
  outfile_path = 'updated_start_unk_flag/updated_out.bw' + str(bw) + '.ns0.sfw0.type33.txt'

  infile = open(infile_path, 'r')
  wordmap = open(word_map_path, 'r')
  fout = open(outfile_path, 'w')

  wordmap_dict = {}
  for line in wordmap.readlines():
      w = line.split()
      if len(w) > 1:
        wordmap_dict[w[1].strip()] = w[0]

  for line in infile.readlines():
      if line.startswith(' '):
          continue
      else:
          w = line.split(':')
          #print w
          k = w[0].strip()
          #print k, ':',
          print >>fout, k, ':',
          v = w[1].split('|')
          l = [x for x in v if x != '\n']
          for i in xrange(len(l)):
            #print l[i], i, '|',
            print >>fout, l[i], i, '|',
          #print '\n'
          print >>fout, '\n'
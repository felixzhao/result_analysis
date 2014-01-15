
import sys

noise_size_list = [1, 2, 3]

for n in noise_size_list:
  infile_path = 'BeamSearch/out.bw10.ns'+ str(n) +'.sfw10.type33.txt'
  word_map_path = 'source/src-33percent/word-map.txt'
  outfile_path = 'updated_start_unk_flag/updated_out.bw10.ns'+ str(n) +'.sfw10.type33.txt'

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
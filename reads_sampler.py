from Bio import SeqIO
from Bio.SeqUtils import GC


def reads_comparer(input_for_list, input_rev_list, number, min_length, max_length, min_quality, max_quality,
                   min_gc_content, max_gc_content, file):

    if min_length <= len(input_for_list[number].seq) == len(input_rev_list[number].seq) < max_length:

        if min_quality <= sum(input_for_list[number].letter_annotations["phred_quality"]) \
                / len(input_for_list[number].letter_annotations["phred_quality"]) < max_quality and \
                min_quality <= sum(input_rev_list[number].letter_annotations["phred_quality"]) \
                / len(input_rev_list[number].letter_annotations["phred_quality"]) < max_quality:

            if min_gc_content <= GC(input_for_list[number].seq) < max_gc_content and \
                    min_gc_content <= GC(input_rev_list[number].seq) < max_gc_content:
                file.write('>' + str(number) + 'f' + '\n' + str(input_for_list[number].seq) + '\n')
                file.write('>' + str(number) + 'r' + '\n' + str(input_rev_list[number].seq) + '\n')
    return 1


def reads_sample(path1, path2, output, number_of_reads, min_gc_content=0, max_gc_content=100,
                 min_length=0, max_length=1000, min_quality=0, max_quality=100, numbers_of_fiels=1):

    # GC-content, length of reads and sequence quality could be as one-boarded or both-boarded characteristics
    # the first way you can place 1 level and sort all reads from or to
    # the second way you can set a range of interesting characteristics

    for_list = list(SeqIO.parse(path1, 'fastq'))
    print('first list parsed')
    rev_list = list(SeqIO.parse(path2, 'fastq'))
    print('second list parsed')
    max_i, j = 0, 0
    for j in range(numbers_of_fiels):
        print('Opening file...')
        way = str(output + '_%s' + '.fasta') % str(j + 1)
        f = open(way, 'w')
        m = 0
        for i in range(max_i, len(for_list)):
            if m < number_of_reads:
                m += reads_comparer(for_list, rev_list, i, min_length, max_length, min_quality, max_quality,
                                    min_gc_content, max_gc_content, f)
            else:
                f.close()
                print('File closed')
                max_i = i
                break


reads_sample('/home/nikolay/Aetau/L002_forward_paired.fq',
             '/home/nikolay/Aetau/L002_reverse_paired.fq',
             '/home/nikolay/Aetau/Script_results/L002_output',
             250000, numbers_of_fiels=4)

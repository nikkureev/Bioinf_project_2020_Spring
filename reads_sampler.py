from Bio import SeqIO
from Bio.SeqUtils import GC


def reads_sample(path1, path2, output, number_of_reads, min_gc_content=0, max_gc_content=100,
                 min_length=0, max_length=1000, min_quality=0, max_quality=100):

    # GC-content, length of reads and sequence quality could be as one-boarded or both-boarded characteristics
    # the first way you can place 1 level and sort all reads from or to
    # the second way you can set a range of interesting characteristics

    m = 0
    with open(output, 'w') as f:
        for_list = list(SeqIO.parse(path1, 'fastq'))
        rev_list = list(SeqIO.parse(path2, 'fastq'))
        while m < number_of_reads:
            if min_length <= len(for_list[m].seq) == len(rev_list[m].seq) < max_length:
                if min_quality <= sum(for_list[m].letter_annotations["phred_quality"]) \
                    / len(for_list[m].letter_annotations["phred_quality"]) < max_quality and \
                        min_quality <= sum(rev_list[m].letter_annotations["phred_quality"]) \
                        / len(rev_list[m].letter_annotations["phred_quality"]) < max_quality:
                    if min_gc_content <= GC(for_list[m].seq) < max_gc_content and \
                            min_gc_content <= GC(rev_list[m].seq) < max_gc_content:
                        f.write('>' + str(m) + 'f' + '\n' + str(for_list[m].seq) + '\n')
                        f.write('>' + str(m) + 'r' + '\n' + str(rev_list[m].seq) + '\n')
            m += 1


reads_sample('/home/nikolay/Aetau/L001_forward_paired.fq',
             '/home/nikolay/Aetau/L001_reverse_paired.fq',
             '/home/nikolay/Aetau/L001_output.fasta',
             250000)

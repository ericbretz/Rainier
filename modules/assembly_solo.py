import gzip
import sys
import pandas as pd
import os

metrics = []
count = 0

class SEQ:
    def __init__(self):
        self.contigs_df  = pd.DataFrame(columns=["contig_name", "length", "prop_gc", "orf_length"])
        self.assemblies_df = pd.DataFrame(columns=["assembly", "n_seqs", "smallest", "largest", "n_bases", "mean_len",
                                                    "n_under_200", "n_over_1k", "n_over_10k", "n_with_orf", "mean_orf_percent",
                                                      "n90", "n70", "n50", "n30", "n10", "gc", "bases_n", "proportion_n"])
        
        self.count            = 0
        self.outdir           = ''
        self.assembly         = ''
        self.file             = ''

        self.smallest         = 0
        self.largest          = 0
        self.n_bases          = 0
        self.mean_len         = 0
        self.n_under_200      = 0
        self.n_over_1k        = 0
        self.n_over_10k       = 0
        self.n_with_orf       = 0
        self.mean_orf_percent = 0
        self.n90              = 0
        self.n70              = 0
        self.n50              = 0
        self.n30              = 0
        self.n10              = 0
        self.gc               = 0
        self.proportion_n     = 0

        self.contig_name      = ''
        self.seq              = ''
        self.length           = 0
        self.count_a          = 0
        self.count_t          = 0
        self.count_g          = 0
        self.count_c          = 0
        self.count_n          = 0
        self.prop_gc          = 0
        self.orf_length       = 0


    def contig_metrics(self):
        if self.contig_name and self.seq:
            self.length     = len(self.seq)
            self.count_a    = self.seq.count('A')
            self.count_t    = self.seq.count('T')
            self.count_g    = self.seq.count('G')
            self.count_c    = self.seq.count('C')
            self.count_n    = self.seq.count('N')
            self.orf_length = self.longest_orf(self.seq)
            self.prop_gc    = round((self.seq.count('G') + self.seq.count('C')) / self.length, 6)
            self.add_contig_metrics()
            self.reset_metrics()
        pass
    
    def assembly_metrics(self):
        self.assembly = os.path.basename(self.file)
        self.smallest = self.contigs_df['length'].min()
        self.largest  = self.contigs_df['length'].max()
        self.n_bases  = self.contigs_df['length'].sum()
        self.mean_len = round(self.contigs_df['length'].mean(), 6)
        self.n_under_200 = len(self.contigs_df[self.contigs_df['length'] < 200])
        self.n_over_1k   = len(self.contigs_df[self.contigs_df['length'] > 1000])
        self.n_over_10k  = len(self.contigs_df[self.contigs_df['length'] > 10000])
        self.n_with_orf  = len(self.contigs_df[self.contigs_df['orf_length'] > 149])
        self.gc = round((self.contigs_df['length'] * self.contigs_df['prop_gc']).sum() / self.contigs_df['length'].sum(), 6)
        self.proportion_n = round(self.count_n / self.n_bases, 6)
        self.mean_orf_percent = round((300 * sum(self.contigs_df['orf_length'])) / (self.count * self.mean_len), 6)

        self.n_metrics()
        self.assembly_df_add()
        return

    def n_metrics(self):
        b90 = int(self.n_bases * 0.9)
        b70 = int(self.n_bases * 0.7)
        b50 = int(self.n_bases * 0.5)
        b30 = int(self.n_bases * 0.3)
        b10 = int(self.n_bases * 0.1)

        sorted_lengths = sorted(self.contigs_df['length'], reverse=True)

        for x in sorted_lengths:
            b90 -= x
            if b90 <= 0:
                self.n90 = x
                break
        for x in sorted_lengths:
            b70 -= x
            if b70 <= 0:
                self.n70 = x
                break
        for x in sorted_lengths:
            b50 -= x
            if b50 <= 0:
                self.n50 = x
                break
        for x in sorted_lengths:
            b30 -= x
            if b30 <= 0:
                self.n30 = x
                break
        for x in sorted_lengths:
            b10 -= x
            if b10 <= 0:
                self.n10 = x
                break

    def assembly_df_add(self):
        new_row = {"assembly": self.assembly, "n_seqs": self.count, "smallest": self.smallest, "largest": self.largest, "n_bases": self.n_bases, "mean_len": self.mean_len,
                    "n_under_200": self.n_under_200, "n_over_1k": self.n_over_1k, "n_over_10k": self.n_over_10k, "n_with_orf": self.n_with_orf, "mean_orf_percent": self.mean_orf_percent,
                    "n90": self.n90, "n70": self.n70, "n50": self.n50, "n30": self.n30, "n10": self.n10, "gc": self.gc, "bases_n": self.count_n, "proportion_n": self.proportion_n}
        self.assemblies_df.loc[len(self.assemblies_df)]= new_row
        return

    def longest_orf(self, seq):
        longest  = 0
        len_list = [0, 0, 0]
        sl       = len(seq)
        str      = seq
        for i in range(sl - 2):
            if str[i:i+3] == 'atg':
                len_list[i % 3] = len_list[i % 3] + 1 if len_list[i % 3] >= 0 else 1
            elif str[i:i+3] in ['tag', 'taa', 'tga']:
                longest = max(longest, len_list[i % 3])
                len_list[i % 3] = -1
            else:
                len_list[i % 3] = len_list[i % 3] + 1 if len_list[i % 3] >= 0 else 0
        longest  = max(longest, max(len_list))
        len_list = [0, 0, 0]
        for i in range(sl - 1, 1, -1):
            if str[i-2:i+1] == 'cat':
                len_list[i % 3] = len_list[i % 3] + 1 if len_list[i % 3] >= 0 else 1
            elif str[i-2:i+1] in ['cta', 'tta', 'tct']:
                longest = max(longest, len_list[i % 3])
                len_list[i % 3] = -1
            else:
                len_list[i % 3] = len_list[i % 3] + 1 if len_list[i % 3] >= 0 else 0
        return max(longest, max(len_list))

    def add_contig_metrics(self):
        new_row = {"contig_name": self.contig_name, "length": self.length, "prop_gc": self.prop_gc, "orf_length": self.orf_length}
        self.contigs_df.loc[len(self.contigs_df)]= new_row
        return
    
    
    def write_contig_df(self):
        contig_f = os.path.join(self.outdir, 'contigs.csv')
        self.contigs_df.to_csv(contig_f, index=False)
        return

    def write_assembly_df(self):
        assembly_f = os.path.join(self.outdir, 'assemblies.csv')
        self.assemblies_df.to_csv(assembly_f, index=False)
        return

    def reset_metrics(self):
        self.contig_name = ''
        self.seq         = ''
        self.length      = 0
        self.prop_gc     = 0
        self.orf_length  = 0
        return
    

def assembly_solo(assembly_f, out_d):
    read        = SEQ()
    read.outdir = out_d
    read.file   = assembly_f

    with open(assembly_f, 'r') as f:
        for line in f:
            if line.startswith('>'):
                read.contig_metrics()
                read.count += 1
                line = line.strip('\n').strip('>')
                read.contig_name = line
                read.seq = ''
            else:
                read.seq += line.upper().strip('\n')
        read.contig_metrics()
        read.write_contig_df()
        read.assembly_metrics()
        read.write_assembly_df()
import __init__
import sys
import argparse
import threading
import time
import random
import psutil
# from modules.run import MAIN
from modules.run_revamp import MAIN

if __name__ == '__main__':
    class PARSER:
        def __init__(self):
            self.color = ''

        def logoprint(self):
            colors = {
                'red': '\033[0;31m',
                # 'green': '\033[0;32m',
                'yellow': '\033[0;33m',
                'blue': '\033[0;34m',
                'purple': '\033[0;35m',
                'cyan': '\033[0;36m'
            }
            C = random.choice(list(colors.values()))
            H = '\033[m'
            self.color = C
            W = '\033[37m'
            
            rversion = f'v{__init__.__version__}'
            rainier_logo = f'''
  {W}┌─{C}███████{W}  ┌─{C}██████{W} ┌─{C}██████{W}┌─{C}██{W}  ┌─{C}██{W}┌─{C}██████{W}┌─{C}████████{W}┌─{C}███████{W} 
  │ {C}██{W}──┐ {C}██{W}┌┘{C}██{W}──┐ {C}██{W}└─┐ {C}██{W}─┘│ {C}███ {W}│ {C}██{W}└─┐ {C}██{W}─┘│ {C}██{W}─────┘│ {C}██{W}──┐ {C}██{W}
  │ {C}██  {W}│ {C}██{W}│ {C}██{W}  │ {C}██{W}  │ {C}██{W}  │ {C}████{W}│ {C}██{W}  │ {C}██{W}  │ {C}██{W}      │ {C}██{W}  │ {C}██{W}
  │ {C}███████{W}┘│ {C}████████{W}  │ {C}██{W}  │ {C}██{W} {C}██{W} {C}██{W}  │ {C}██{W}  │ {C}█████{W}   │ {C}███████{W}┘
  │ {C}▓▓{W}──┐ {C}▓▓{W}│ {C}▓▓{W}──┐ {C}▓▓{W}  │ {C}▓▓{W}  │ {C}▓▓{W}┐ {C}▓▓▓▓{W}  │ {C}▓▓{W}  │ {C}▓▓{W}──┘   │ {C}▓▓{W}──┐ {C}▓▓{W}
  │ {C}▒▒{W}  │ {C}▒▒{W}│ {C}▒▒{W}  │ {C}▒▒{W}  │ {C}▒▒{W}  │ {C}▒▒{W}└┐ {C}▒▒▒{W}  │ {C}▒▒{W}  │ {C}▒▒{W}      │ {C}▒▒{W}  │ {C}▒▒{W}
  │ {C}░░{W}  │ {C}░░{W}│ {C}░░{W}  │ {C}░░{W}┌─{C}░░░░░░{W}│ {C}░░{W} └┐ {C}░░{W}┌─{C}░░░░░░{W}│ {C}░░░░░░░░{W}│ {C}░░{W}  │ {C}░░{W}
  └──┘  └──┘└──┘  └──┘└──────┘└──┘  └──┘└──────┘└────────┘└──┘  └──┘
{W}{"Quality analysis for de-novo transcriptome assemblies":^66}
{W}{"EC Bretz":>66}
{W}{rversion:>66}\033[0m'''

            print(rainier_logo)

        def helpoptions(self):

            topbar = f'{self.color}  ┌{"─" * 23}\033[m   Help Options   {self.color}{"─" * 23}┐\033[m'
            bottombar = f'{self.color}  └{"─" * 64}┘\033[m'

            modebar = f'{self.color}  ┌{"─" * 23}\033[m    Mode Types    {self.color}{"─" * 23}┐\033[m'
            extrabar = f'{self.color}  ┌{"─" * 23}\033[m     #Threads     {self.color}{"─" * 23}┐\033[m'
            options = {
                'Assembly': ['--assembly', '-a', 'Path to assembly file'],
                'Left Reads': ['--left', '-l', 'Path to left reads file'],
                'Right Reads': ['--right', '-r', 'Path to right reads file'],
                'Reference': ['--reference', '-r', 'Path to reference file'],
                'Output Directory': ['--outdir', '-o', 'Path to output directory'],
                'Threads': ['--threads', '-t', 'Number of threads to use'],
                'Clutter': ['--clutter', '-c', 'Remove intermediate files'],
                'Help': ['--help', '-h', 'Display this help message']
            }
            modes = {
                'Assembly': ['-a', 'Only run assembly analysis'],
                'Reads': ['-a -l -r', 'Run assembly with reads analysis'],
                'All': ['-a -l -r -f', 'Run assembly with reads and reference'],
                'Reference': ['-a -f', 'Run assembly with reference analysis'],
            }

            print(topbar)
            for k,v in options.items():
                print(f'{self.color}  │\033[m {v[0]:<20}{v[1]:<15}{v[2]:<28}{self.color}│\033[m')
            print(bottombar)
            print(modebar)
            for k,v in modes.items():
                body = f'{self.color}  │\033[m {v[0]:<20}{v[1]:<5}{self.color}'
                length = 84 - len(str(body))
                print(f'{body}{" " * (length)}│\033[m')
            print(bottombar)

            print(extrabar)
            logical = psutil.cpu_count(logical=True)
            physical = psutil.cpu_count(logical=False)
            threadslabel = f'{self.color}  │\033[m Threads: {self.color}'
            logbody = f'{self.color}  │\033[m     Logical: {logical}'
            physbody = f'{self.color}  │\033[m     Physical: {physical}'
            threalen = 84 - len(str(threadslabel))
            loglen = 77 - len(str(logbody))
            physlen = 77 - len(str(physbody))
            print(f'{threadslabel}{self.color}{" " * threalen}│\033[m')
            print(f'{logbody}{" " * loglen}{self.color}│\033[m')
            print(f'{physbody}{" " * physlen}{self.color}│\033[m')
            print(bottombar)

        def parser(self):
            parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.RawTextHelpFormatter)
            parser.add_argument('--assembly', '-a', type=str , help='Assembly file')
            parser.add_argument('--left', '-l', type=str , help='Left reads file')
            parser.add_argument('--right', '-r', type=str , help='Right reads file')
            parser.add_argument('--reference', '-f', type=str , help='Reference file')
            parser.add_argument('--output', '-o', type=str , help='Output directory')
            parser.add_argument('--threads', '-t', type=int , help='Number of threads')
            parser.add_argument('--clutter', '-c', action='store_true', help='Remove clutter from output directory')
            parser.add_argument('--help', '-h', action='store_true', help='Display this help message')

            args = parser.parse_args()

            def parameters():
                topbar = f'{self.color}  ┌{"─" * 64}┐\033[m'
                bottombar = f'{self.color}  └{"─" * 64}┘\033[m'
                print(topbar)
                for k,v in args.__dict__.items():
                    if v:
                        xlen = 64 - len(str(k)) - 40
                        x = ' ' * xlen
                        y = 64 - len(str(v)[-30:]) - 25
                        if len(str(v)) >= 30:
                            v = f'...{str(v)[-27:]}'
                        line =  f'{self.color}  │\033[m {k.capitalize()}{x}{str(v)[-30:]}{self.color}{" "*y}│\033[m'
                        print(line)
                print(bottombar)
                print('')

            if args.help:
                self.helpoptions()
                sys.exit()

            elif len(sys.argv) != 1:

                rainier_start           = MAIN()
                rainier_start.ASSEMBLY  = args.assembly if args.assembly else ''
                rainier_start.LEFT      = args.left if args.left else ''
                rainier_start.RIGHT     = args.right if args.right else ''
                rainier_start.REFERENCE = args.reference if args.reference else ''
                rainier_start.THREADS   = args.threads if args.threads else 1
                rainier_start.OUTDIR    = args.output if args.output else ''
                rainier_start.CLUTTER   = args.clutter if args.clutter else False
                parameters()
                rainier_start.LOGOCOLOR = self.color
                rainier_start.run()
            else:
                self.helpoptions()
                sys.exit()

    
    rainierparser = PARSER()
    rainierparser.logoprint()
    rainierparser.parser()

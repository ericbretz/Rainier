from datetime import datetime

date_time = datetime.now()
y = str(date_time.year)

__major__ = 0
__minor__ = 8
__patch__ = 4
__script_name__ = 'Rainier'
__version__ = f'{__major__}.{__minor__}.{__patch__}'
__description__ = ('Quality analysis for de-novo transcriptome assemblies')
__author__ = 'Eric C. Bretz'
__author_email__ = 'ebretz2@uic.edu'
__url__ = 'https://github.com/ericbretz'
__copyright__ = 'Copyright \u00A9 ' + __author__ + ', ' + y
__license__ = 'GNU General Public License Version 3'

__all__ = ['__author__', '__author_email__', '__url__', '__description__', '__script_name__', '__version__']


# Copyright (c) 2012-2015, GEM Foundation.
#
# This program is free software: you can redistribute it and/or modify
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from django.shortcuts import render
from django.template import RequestContext
import openquakeplatform_taxonomy


def taxonomy(request, pg=None, **kwargs):
    if pg:
        cont_f = os.path.join(os.path.dirname(openquakeplatform_taxonomy.__file__), 'data', pg + '.html')
        
        with open(cont_f, 'r') as f:
            cont = f.read()
            title = cont.split('\n', 1)[0].replace('<h2>', '').replace('</h2>', '').replace('\n', '')

            cont = cont.replace(' src="img/', ' src="/static/taxonomy/img/')
            return render(request, "taxonomy/taxonomy.html", dict(title=title, cont=cont))
    else:
        id = request.GET.get('id', '')
        return render(request, "taxonomy/index.html", dict(id=id))

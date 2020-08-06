from django import template


register = template.Library()

@register.filter('continue')
def continue_(loop):
    '''Continues a loop by jumping to its beginning.

    The 'continue' filter is used within a loop and takes as input a loop
    variable, e.g. 'forloop' in case of a for loop. It can also be used (and is
    mostly useful) for nested loops by passing the appropriate loop variable,
    e.g. ``forloop.parentloop|continue``. For example::

        {% for key,values in mapping.iteritems %}<br/>
            {% for value in values %}
                {{ key }}: {{ value }}<br/>
                {% if value|divisibleby:3  %}
                    {{ value }} is divisible by 3<br/>
                    {{ forloop.parentloop|continue }}
                {% endif %}
            {% endfor %}
            {{ key }}: No value divisible by 3<br/>
        {% endfor %}
    '''


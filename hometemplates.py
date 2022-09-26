Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
{% extends 'base.html' %}
{#{% load staticfiles %}#}

{% block head %}

{#    <link rel="stylesheet" href="//assets/stylesheets/bootstrap.min.css" />#}
{#    <link rel="stylesheet" href="//assets/stylesheets/bootstrap-responsive.min.css" />#}
{#    <link rel="stylesheet" href="//assets/stylesheets/application.css" />#}
{##}
{#    <script src="//assets/javascripts/jquery-1.9.1.js"></script>#}
{#    <script src="//assets/javascripts/calculator.js"></script>#}
{% endblock %}


{% block body %}

  <div class="container text-center">

    <h1>Calculator</h1>
      <br/>
      <br/>


      <form action="" method="post">
          {% csrf_token %}
          {{ form.as_p }}



          <button type="submit" name="add">ADD</button>
          <button type="submit" name="sub">SUB</button>
          <button type="submit" name="mul">MUL</button>
          <button type="submit" name="div">DIV</button>



      </form>

      <br/>
      <br/>
       <h3>Result:  {{ result }}</h3>


{#      <div class="hero-unit" id="calculator-wrapper">#}
{#        <div class="row-fluid">#}
{#          <div class="span8">#}
{#            <div id="calculator-screen" class="uneditable-input"></div>#}
{#          </div>#}
{#          <div class="span1" style="text-align: center;">#}
{#            <div class="visible-phone">#}
{#              =#}
{#            </div>#}
{#            <div class="hidden-phone">#}
{#              =#}
{#            </div>#}
{#          </div>#}
{#          <div class="span3">#}
{#            <div id="calculator-result"  class="uneditable-input">0</div>#}
{#          </div>#}
{#        </div>#}
{##}
{#      </div>#}
{##}
{#      <div class="row-fluid">#}
{##}
{#        <div class="span10 well">#}
{#          <div id="calc-board">#}
{#            <div class="row-fluid">#}
{#              <a href="#" class="btn" data-constant="SIN" data-key="115">sin</a>#}
{#              <a href="#" class="btn" data-constant="COS" data-key="99">cos</a>#}
{#              <a href="#" class="btn" data-constant="MOD" data-key="109">md</a>#}
{#              <a href="#" class="btn btn-danger" data-method="reset" data-key="8">C</a>#}
{#            </div>#}
{#            <div class="row-fluid">#}
{#              <a href="#" class="btn" data-key="55">7</a>#}
{#              <a href="#" class="btn" data-key="56">8</a>#}
{#              <a href="#" class="btn" data-key="57">9</a>#}
{#              <a href="#" class="btn" data-constant="BRO" data-key="40">(</a>#}
{#              <a href="#" class="btn" data-constant="BRC" data-key="41">)</a>#}
{#            </div>#}
{#            <div class="row-fluid">#}
{#              <a href="#" class="btn" data-key="52">4</a>#}
{#              <a href="#" class="btn" data-key="53">5</a>#}
{#              <a href="#" class="btn" data-key="54">6</a>#}
{#              <a href="#" class="btn" data-constant="MIN" data-key="45">-</a>#}
{#              <a href="#" class="btn" data-constant="SUM" data-key="43">+</a>#}
{#            </div>#}
{#            <div class="row-fluid">#}
{#              <a href="#" class="btn" data-key="49">1</a>#}
{#              <a href="#" class="btn" data-key="50">2</a>#}
{#              <a href="#" class="btn" data-key="51">3</a>#}
{#              <a href="#" class="btn" data-constant="DIV" data-key="47">/</a>#}
{#              <a href="#" class="btn" data-constant="MULT" data-key="42">*</a>#}
{#            </div>#}
{#            <div class="row-fluid">#}
{#              <a href="#" class="btn" data-key="46">.</a>#}
{#              <a href="#" class="btn" data-key="48">0</a>#}
{#              <a href="#" class="btn" data-constant="PROC" data-key="37">%</a>#}
{#              <a href="#" class="btn btn-primary" data-method="calculate" data-key="61">=</a>#}
{#            </div>#}
{#          </div>#}
{#        </div>#}
{##}
{#        <div class="span6 well">#}
{#          <legend>History</legend>#}
{#          <div id="calc-panel">#}
{#            <div id="calc-history">#}
{#              <ol id="calc-history-list"></ol>#}
{#            </div>#}
{#          </div>#}
{#        </div>#}
{#        <hr>#}
{##}
{#      </div>#}
    </div>



{% endblock %}
</html>
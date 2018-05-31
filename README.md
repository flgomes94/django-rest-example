<h1>Django Rest Framework</h1>
<p>Nesse exemplo, desenvolvi um sistema do tipo CRUD utilizando Django e Django Rest Framework com sistema de autenticação. O sistema tem um funcionamento bem simples, permitindo assim criar usuários, listar todos os usuários, atualizar algum específico ou deletar, utilizando autenticação, onde apenas o usuário que criou a entrada pode efetuar as outras alterações.</p>

<h2>Recomendação</h2>
<ul>
  <li>Django+=2.0.5</li>
  <li>Python+=3.6</li>
  <li>PyCharm Community+=2017.3.4</li>
</ul>
<h2>Passos</h2>
<p>
1. Crie uma virtualenv com o comando:</br>
<blockquote>virtualenv -p python3 env</blockquote></br></p>
<p>2. Execute a virtualenv</br>
<blockquote>. env/bin/activate</blockquote></p>
<p>3. Instale as dependências do projeto que estão no arquivo requirements.txt</br>
<blockquote>pip install -r requirements.txt</blockquote></p>
<p>3. Efetue o migrations e o migrate dentro do projeto contatos</br>
<blockquote>python manage.py makemigrations</br>
python manage.py makemigrations pessoas</br>
python manade.py migrate</blockquote></p>
<p>4. Crie um superuser</br>
<blockquote>python manage.py createsuperuser</br>
</blockquote></p>
<p>Pronto :)</p>
<h2>Comandos (utilizando o httpie no ubuntu 16.04) e usuário criado no superuser</h2>
<p>LISTAR: <blockquote><p>http -a user:password GET http://127.0.0.1:8000/pessoas/</p></blockquote></p>
<p>INSERIR: <blockquote><p>http -a user:password POST http://127.0.0.1:8000/pessoas/ nome="nome para salvar" telefone="telefone para salvar" email="algum email"</p></blockquote></p>
<p>ATUALIZAR: <blockquote><p>http -a user:password PUT http://127.0.0.1:8000/pessoas/<id>  ... (parametros para alterar)</p></blockquote></p>
<p>DELETAR: <blockquote><p>http -a user:password PUT http://127.0.0.1:8000/pessoas/<id>  ... (entrada para apagar)</p></blockquote></p>


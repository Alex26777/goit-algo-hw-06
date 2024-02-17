# goit-algo-hw-06 
Коментарі до Завдання 2:
У цьому завданні ми застосували два фундаментальні алгоритми пошуку: алгоритм пошуку в глибину (DFS) та алгоритм пошуку в ширину (BFS), до графа, створеного у Завданні 1.

Алгоритм DFS (Depth-First Search) ітеративно проникає якомога глибше в граф вздовж кожної гілки перед "зворотним відступом". Цей метод дозволяє знаходити шляхи, що можуть виявитися довшими за найкоротший можливий, оскільки DFS не гарантує знаходження найкоротшого шляху.

Натомість, BFS (Breadth-First Search) працює шар за шаром, рівномірно розширюючись у всі сторони. Він гарантує знаходження найкоротшого шляху в графі, якщо такий існує, тому що він вивчає всі можливі шляхи, які мають однакову кількість кроків, перед тим як переходити до шляхів, що мають більше кроків.

Під час порівняння результатів, отриманих обома алгоритмами на одному й тому ж графі, ми помітили, що BFS завжди надає найкоротший шлях між двома вершинами, в той час як DFS може надати один із можливих шляхів, який не обов'язково є найкоротшим.

Різниця в отриманих шляхах зумовлена стратегіями, які використовуються в кожному з алгоритмів для проходження графа. BFS використовує чергу для зберігання всіх сусідніх вершин для подальшого візиту, що забезпечує рівномірне "розповсюдження" по всьому графу. DFS використовує стек, що призводить до негайного "занурення" в одну з гілок графа до самого кінця, перш ніж переходити до іншої гілки.

В результаті, BFS є кращим вибором для знаходження найкоротших шляхів у невагових графах, тоді як DFS може бути корисним для завдань, які вимагають вивчення всіх можливих шляхів або для знаходження компонентів зв'язності в графі.

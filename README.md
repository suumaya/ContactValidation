# ContactValidation
This way of store and read database is the optimal way to prevent SQL injection

Below are some examples of accepted inputs for Name:
'Bruce Schneier' 
'Schneier, Bruce' 
'Schneier, Bruce Wayne' 
"O'Malley, John F."
"John O'Malley-Smith"
'Cher'

Below are some examples of unaccepted inputs for Name:
"Ron O''Henry"
"Ron O'Henry-Smith-Barnes" 
"L33t Hacker" 
'<Script>alert("XSS")</Script>'
"Brad Everett Samuel Smith"
"select * from users;"
 
Below are some examples of accepted inputs for Phone number:

"12345" 
"(703)111-2121" 
"123-1234" 
"+1(703)111-2121"
"+32 (21) 212-2324" 
"1(703)123-1234" 
"011 701 111 1234" 
"12345.12345"
"011 1 703 111 1234"

Below are some examples of unaccepted inputs for Phone number:

"123"
"1/703/123/1234"
"Nr 102-123-1234" '<script>alert("XSS")</script>' "7031111234"
"+1234 (201) 123-1234"
"(001) 123-1234"
"+01 (703) 123-1234"
"(703) 123-1234 ext 204"

Below are some examples of accepted inputs for street address:

795 E DRAGRAM Drive, TUCSON, AZ 85705-7598 795 E DRAGRAM Dr., TUCSON, AZ 85705
770W DRAGRAM Drive # 321, TUCSON, AZ 85703 2430 7th St, Washington, DC 20521-2430
Below are some examples of unaccepted inputs for street address:
E DRAGRAM Drive, TUCSON, AZ 85705-7598 795 E DRAGRAM Dr, TUCSON, AZ 8570
770W DRAGRAM Drive # 321, TUCSON, 85703 2430 7th St, DC 20521-2430

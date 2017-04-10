# install nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh | bash
    # useable nodejs version
    nvm ls-remote
    # install nodejs
    nvm install <version>
    # installed nodejs
    nvm ls
    # selected nodejs
    nvm use <version>
    # set default version
    nvm alias default <version>
    # uninstall nodejs
    nvm uninstall <version>
# install nodejs
nvm install <version>
nvm use <version>

# install express-generator
npm install express-generator -g

# create express app
express <appname>

# install dependencies
npm install

# test
linux: DEBUG=<appname> npm start
window: set DEBUG=<appname> & npm start
http://localhost:3000/

# run & stop service
forever start <script>
forever list
forever stop <uid>
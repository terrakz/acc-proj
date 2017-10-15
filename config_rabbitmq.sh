      #!/usr/bash
      #start rabbitmq-server
      rabbitmq-server
      # add user 'acc5' with password 'acc12345'
      rabbitmqctl add_user acc5 acc12345
      # add virtual host acc5_vhost'
      rabbitmqctl add_vhost acc5_vhost
      # add user tag acc5_tag' for user acc5'
      rabbitmqctl set_user_tags acc5 acc5_tag
      # set permission for user 'acc5' on virtual host acc5_vhost'
      rabbitmqctl set_permissions -p acc5_vhost acc5 ".*" ".*" ".*"

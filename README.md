<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-rpo_epel.svg)](https://github.com/while-true-do/ansible-role-rpo_epel/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-rpo_epel.svg)](https://github.com/while-true-do/ansible-role-rpo_epel/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-rpo_epel.svg)](https://github.com/while-true-do/ansible-role-rpo_epel/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-rpo_epel.svg)](https://github.com/while-true-do/ansible-role-rpo_epel/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-rpo_epel.svg)](https://travis-ci.com/while-true-do/ansible-role-rpo_epel)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-rpo_epel%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/rpo_epel)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-rpo_epel%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/rpo_epel)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-rpo_epel%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/rpo_epel)

# Ansible Role: rpo_epel

An Ansible Role to install and enable Extra Packages for Enterprise Linux
[(EPEL)](https://fedoraproject.org/wiki/EPEL) repositories.

## Motivation

[EPEL](https://fedoraproject.org/wiki/EPEL) Repositories are needed for many
packages in RedHat and CentOS.

## Description

This role is installing and configuring EPEL.

-   install epel-release
-   enable epel and epel-testing

## Requirements

On RHEL 7 it is recommended to also enable the `optional`, `extras`, and `HA`
repositories since EPEL packages may depend on packages from these repositories.
The role offers an option to handle this, by default.

Used Modules:

-   [Ansible yum Module](https://docs.ansible.com/ansible/latest/modules/yum_module.html)
-   [Ansible ini_file Module](https://docs.ansible.com/ansible/latest/modules/ini_file_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/rpo_epel)
```
ansible-galaxy install while_true_do.rpo_epel
```

Install from [Github](https://github.com/while-true-do/ansible-role-rpo_epel)
```
git clone https://github.com/while-true-do/ansible-role-rpo_epel.git while_true_do.rpo_epel
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.rpo_epel

## Package Management
# Defaults are based on CentOS Linux
wtd_rpo_epel_package: "epel-release"
# State can be present|latest|absent
wtd_rpo_epel_package_state: "present"

## Configuration Management
# Enable or disable installed repositories
wtd_rpo_epel_conf_enabled: "1"
wtd_rpo_epel_conf_testing_enabled: "0"

# Only for Red Hat
# Enable the recommended Red Hat Repository Subscriptions
# State can be enabled|disabled|unmanaged
wtd_rpo_epel_conf_rh_extras_repo_state: "enabled"
wtd_rpo_epel_conf_rh_optional_repo_state: "enabled"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.rpo_epel
```

#### Enable EPEL Testing

```
- hosts: all
  roles:
    - role: while_true_do.rpo_epel
      wtd_rpo_epel_conf_testing_enabled: "1"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-rpo_epel/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-rpo_epel/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>

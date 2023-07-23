#!/bin/bash

# Check if the script is being run with root privileges
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run with root privileges. Please use sudo."
  exit 1
fi

# Check the package manager (yum or dnf) to use
if command -v dnf &>/dev/null; then
  PACKAGE_MANAGER="dnf"
elif command -v yum &>/dev/null; then
  PACKAGE_MANAGER="yum"
else
  echo "Error: Neither yum nor dnf package manager is installed on your system."
  exit 1
fi

# Update the package manager
$PACKAGE_MANAGER update -y

# Install the necessary packages to enable additional repositories
$PACKAGE_MANAGER install -y epel-release

# Enable the optional and extras repositories (if not already enabled)
if [ "$PACKAGE_MANAGER" == "yum" ]; then
  $PACKAGE_MANAGER-config-manager --set-enabled rhel-7-server-optional-rpms
  $PACKAGE_MANAGER-config-manager --set-enabled rhel-7-server-extras-rpms
else
  $PACKAGE_MANAGER config-manager --set-enabled codeready-builder-for-rhel-8-x86_64-rpms
  $PACKAGE_MANAGER config-manager --set-enabled extras-rhel-8-x86_64
fi

# Install Python 3 and development tools
$PACKAGE_MANAGER install -y python3 python3-devel

# Update pip to the latest version
pip3 install --upgrade pip

echo "Python 3 installation completed successfully."

#install docker module for python
pip3 install docker

echo "Docker module installation completed successfully."

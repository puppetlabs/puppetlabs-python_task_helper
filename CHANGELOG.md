<!-- markdownlint-disable MD024 -->
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org).

## [v1.0.0](https://github.com/puppetlabs/puppetlabs-python_task_helper/tree/v1.0.0) - 2026-09-10

[Full Changelog](https://github.com/puppetlabs/puppetlabs-python_task_helper/compare/0.6.0...v1.0.0)

### Changed

- (BOLT-193): python_task_helper pdk update to pupet 9 [#22](https://github.com/puppetlabs/puppetlabs-python_task_helper/pull/22) ([gavindidrichsen](https://github.com/gavindidrichsen))

## [v0.6.0]()

## New features

- Bump maximum Puppet version to include 8.x

## Changes

- Updated module with `PDK update` to ensure it consumes current templates

## Release 0.5.0

### New features

- Bump maximum Puppet version to include 7.x

## Release 0.4.0

### New features

- Added a `debug` method to add debugging statements to the `details` field of a `TaskError`.

- Added a `debug_statements` method to retrieve the current list of debugging statements.

## Release 0.3.0

### Bug fixes

- Previously error hashes were not wrapped under an `_error` key causing bolt to ignore underlying error message. Now error hashes are wrapped under the expected `_error` key.

## Release 0.2.0

### Changes

- Helper files should go in the `files` directory of a module to prevent them from being added to the puppet ruby loadpath or seen as tasks.

## Release 0.1.3

### Bug fixes

- Task now uses exit code 1 when exiting due to an exception.

## Release 0.1.2

### Bug fixes

- Fix module metadata to include required keys.

## Release 0.1.1

### Bug fixes

- Fix packaging so automation to ship the module to the Forge works.

## Release 0.1.0

### New features

- Initial release of TaskHelper class to assist with writing Puppet Tasks in Python.

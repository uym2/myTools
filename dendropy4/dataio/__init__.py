#! /usr/bin/env python

##############################################################################
##  DendroPy Phylogenetic Computing Library.
##
##  Copyright 2010-2015 Jeet Sukumaran and Mark T. Holder.
##  All rights reserved.
##
##  See "LICENSE.rst" for terms and conditions of usage.
##
##  If you use this work or any portion thereof in published work,
##  please cite it as:
##
##     Sukumaran, J. and M. T. Holder. 2010. DendroPy: a Python library
##     for phylogenetic computing. Bioinformatics 26: 1569-1571.
##
##############################################################################

import collections
from dendropy4.dataio import newickreader
from dendropy4.dataio import newickwriter
from dendropy4.dataio import newickyielder
from dendropy4.dataio import fastareader
from dendropy4.dataio import fastawriter
from dendropy4.dataio import nexusreader
from dendropy4.dataio import nexuswriter
from dendropy4.dataio import nexusyielder
from dendropy4.dataio import nexmlreader
from dendropy4.dataio import nexmlwriter
from dendropy4.dataio import nexmlyielder
from dendropy4.dataio import phylipreader
from dendropy4.dataio import phylipwriter
from dendropy4.utility import container

_IOServices = collections.namedtuple(
        "_IOServices",
        ["reader", "writer", "tree_yielder"]
        )

_IO_SERVICE_REGISTRY = container.CaseInsensitiveDict()
_IO_SERVICE_REGISTRY["newick"] = _IOServices(newickreader.NewickReader, newickwriter.NewickWriter, newickyielder.NewickTreeDataYielder)
_IO_SERVICE_REGISTRY["nexus"] = _IOServices(nexusreader.NexusReader, nexuswriter.NexusWriter, nexusyielder.NexusTreeDataYielder)
_IO_SERVICE_REGISTRY["nexus/newick"] = _IOServices(None, None, nexusyielder.NexusNewickTreeDataYielder)
_IO_SERVICE_REGISTRY["nexml"] = _IOServices(nexmlreader.NexmlReader, nexmlwriter.NexmlWriter, nexmlyielder.NexmlTreeDataYielder)
_IO_SERVICE_REGISTRY["fasta"] = _IOServices(fastareader.FastaReader, fastawriter.FastaWriter, None)
_IO_SERVICE_REGISTRY["dnafasta"] = _IOServices(fastareader.DnaFastaReader, fastawriter.FastaWriter, None)
_IO_SERVICE_REGISTRY["rnafasta"] = _IOServices(fastareader.RnaFastaReader, fastawriter.FastaWriter, None)
_IO_SERVICE_REGISTRY["proteinfasta"] = _IOServices(fastareader.ProteinFastaReader, fastawriter.FastaWriter, None)
_IO_SERVICE_REGISTRY["phylip"] = _IOServices(phylipreader.PhylipReader, phylipwriter.PhylipWriter, None)

def get_reader(schema, **kwargs):
    try:
        reader_type =_IO_SERVICE_REGISTRY[schema].reader
        if reader_type is None:
            raise KeyError
        reader = reader_type(**kwargs)
        return reader
    except KeyError:
        raise NotImplementedError("'{}' is not a supported data reading schema".format(schema))

def get_writer(
        schema,
        **kwargs):
    try:
        writer_type =_IO_SERVICE_REGISTRY[schema].writer
        if writer_type is None:
            raise KeyError
        writer = writer_type(**kwargs)
        return writer
    except KeyError:
        raise NotImplementedError("'{}' is not a supported data writing schema".format(schema))

def get_tree_yielder(
        files,
        schema,
        taxon_namespace,
        tree_type,
        **kwargs):
    try:
        yielder_type =_IO_SERVICE_REGISTRY[schema].tree_yielder
        if yielder_type is None:
            raise KeyError
        yielder = yielder_type(
                files=files,
                taxon_namespace=taxon_namespace,
                tree_type=tree_type,
                **kwargs)
        return yielder
    except KeyError:
        raise NotImplementedError("'{}' is not a supported data yielding schema".format(schema))

def register_service(schema, reader=None, writer=None, tree_yielder=None):
    global _IO_SERVICE_REGISTRY
    _IO_SERVICE_REGISTRY[schema] = _IOServices(reader, writer, tree_yielder)

def register_reader(schema, reader):
    global _IO_SERVICE_REGISTRY
    try:
        current = _IO_SERVICE_REGISTRY[schema]
        register_service(schema=schema,
                reader=reader,
                writer=current.writer,
                tree_yielder=current.tree_yielder)
    except KeyError:
        register_service(schema=schema, reader=reader)

